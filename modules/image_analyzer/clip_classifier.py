

"""
CLIP-based Image Classifier for Automotive Technical Diagrams
Option 2: Single-stage classification with multi-prompt text ensembles and
targeted post-classification checks to reduce common confusions:
- HMI DISPLAY LAYOUTS ↔ TELLTALE ICONS
- FLOWCHART DIAGRAMS ↔ TECHNICAL SPECIFICATIONS
- COLOR AND GRADIENTS ↔ TECHNICAL SPECIFICATIONS
- TABLE WITH TELLTALES ↔ CONFIGURATION TABLES (extra guard)

Uses original OpenAI CLIP library for compatibility.
"""

import os
import clip
import torch
import numpy as np
from PIL import Image, ImageFilter   # <-- added ImageFilter for edge-density tiebreaker
from datetime import datetime
from typing import List, Dict, Tuple


def _l2_normalize(x: torch.Tensor, dim: int = -1, eps: float = 1e-12) -> torch.Tensor:
    return x / (x.norm(dim=dim, keepdim=True) + eps)


class CLIPImageClassifier:
    def __init__(
        self,
        model_names=("ViT-B/32",),
        device="cpu",
        model_weights=None,
        temperature=0.7,  # default sharper separation
    ):
        """
        Initialize one or more CLIP models for image classification (ensemble)

        Args:
            model_names (tuple|list|str): One model or list/tuple of CLIP model names.
                                          Examples: "ViT-B/32", ["ViT-B/32", "ViT-L/14"]
            device (str): 'cpu' or 'cuda'
            model_weights (list[float]|None): Optional weights per model. If None, uniform average.
            temperature (float): Temperature scaling applied to logits before softmax.
                                 Lower (e.g., 0.05–0.3) => sharper separation.
        """
        self.device = device
        self.temperature = float(temperature)

        # -----------------------------
        # BLACK-BACKGROUND RESTRICTION
        # -----------------------------
        self.black_bg_enabled    = True   # master switch for the rule
        self.dark_bg_threshold   = 0.60   # fraction of pixels < dark_pixel_thr to trigger rule
        self.dark_pixel_thr      = 40     # grayscale cutoff [0..255] for "dark" pixels
        self.black_logit_tie     = 0.02   # if top-2 logits within this, use probes to decide
        self.edge_density_tie    = 0.015  # HMI >= this, Telltale < this (tiebreak)
        self.black_probe_strong  = 0.12   # strong COLOR_GRADIENT probe delta over HMI/Telltale

        # Normalize model_names to list
        if isinstance(model_names, str):
            model_names = [model_names]
        self.model_names = list(model_names)

        # Optional model weights (normalized)
        if model_weights is not None:
            assert len(model_weights) == len(self.model_names), "model_weights must match model_names length"
            w = torch.tensor(model_weights, dtype=torch.float32)
            self.model_weights = (w / w.sum()).tolist()
        else:
            self.model_weights = [1.0 / len(self.model_names)] * len(self.model_names)

        print(f"Loading CLIP models: {', '.join(self.model_names)} on {self.device}")
        self.models = []
        self.preprocess_fns = []

        # Load each model (and its preprocess) separately
        for name in self.model_names:
            try:
                model, preprocess = clip.load(name, device=self.device, jit=False)
                if self.device == "cuda":
                    model = model.half()  # Use half precision on GPU for speed/memory
                model.eval()
                self.models.append(model)
                self.preprocess_fns.append(preprocess)
                print(f"  Successfully loaded {name}")
            except Exception as e:
                print(f"  Error loading {name}: {e}")
                raise e

        # === CATEGORIES ===
        self.categories: Dict[str, str] = {
            # UPDATED: HMI DISPLAY LAYOUTS
            "HMI DISPLAY LAYOUTS": (
                "A full instrument-cluster screen showing multiple UI regions together (speed/RPM/fuel/warnings). "
                "A single cohesive dashboard display, NOT a lone warning icon and NOT a blocky flowchart of boxes and arrows."
            ),

            # UPDATED: CONFIGURATION TABLES
            "CONFIGURATION TABLES": (
                "A technical table with rows and columns whose cells contain only text or numbers. "
                "May include borders, headers, or colored/shaded text BUT NOT COLORED ICONS "
                "but NO pictogram shapes or dashboard symbols. No icon silhouettes in any cell."
            ),

            "MULTI-CONDITION LOGIC": (
                "A logic-gate diagram combining conditions with AND and OR gate symbols. "
                "Rectangular condition blocks feed into gate icons; outputs chain through gates. Not a module block diagram."
            ),

            "SYSTEM ARCHITECTURE DIAGRAMS": (
                "A block diagram of modules (ECUs, sensors, controllers) as rectangular boxes connected by lines or arrows. "
                "Focus on components and data or wiring connections; no logic gate symbols."
            ),

            # UPDATED: STATE FLOW DIAGRAMS
            "STATE FLOW DIAGRAMS": (
                "A state machine diagram with circular/oval states connected by arrows and labeled transitions. "
                "Emphasis on state bubbles and directional connectors. NOT a waveform with a horizontal time axis."
            ),

            "FLOWCHART DIAGRAMS": (
                "Process flow diagrams showing sequential steps and decision logic with connected shapes. "
                "Contains rectangular process boxes, diamond decisions with Yes/No branches, start/end terminators, and arrows for workflow. "
                "Must not contain a horizontal time axis with stacked HIGH/LOW waveform rows."
            ),

            # UPDATED: TECHNICAL SPECIFICATIONS
            "TECHNICAL SPECIFICATIONS": (
                "A document-style page dominated by paragraphs, bullet lists, or headings. "
                "May include small text-only tables, but the page is mostly text blocks. "
                "NOT a dense spreadsheet grid and NOT a table of pictogram icons; no dashboard symbol shapes."
            ),

            "WIRING &amp; SIGNAL DIAGRAMS": "Electrical wiring schematic with wires, connectors, pins, and circuit lines.",

            "TIMING DIAGRAMS": (
                "Digital timing diagram with a horizontal time axis, stacked HIGH/LOW waveform rows, "
                "rectangular step transitions, and vertical alignment guides. Shows signal states over time, "
                "with synchronized markers and temporal relationships. Not a flowchart or wiring schematic."
            ),

            "TIMING – ANALOG / THRESHOLD": (
                "A plot versus time or parameter with axes and units. "
                "Single or few continuous traces (ramps, slopes) and threshold markers, or ON/OFF versus a non‑time variable such as speed or temperature."
            ),

            # UPDATED: TABLE WITH TELLTALES
            "TABLE WITH TELLTALES": (
                "A table that contains automotive warning pictograms INSIDE its cells. "
                "At least one cell shows a recognizable colored image with an icon (battery, oil lamp, ABS, seatbelt), i.e., a drawn symbol with an outline. "
                "Not just colored or shaded cells—must be a visible pictogram."
            ),

            "COLOR AND GRADIENTS": "Color chart, gradient scale, or color calibration pattern. No text or icons.",
            "TELLTALE ICONS AND INDICATORS":  "Single isolated car warning icon or symbol on a plain background with no other dashboard elements. Only one warning light (battery, oil, temperature, etc.).",
            "OTHERS": "Image that does not match any of the above categories"
        }

        self.category_names: List[str] = list(self.categories.keys())

        # === MULTI-PROMPT BANK per category ===
        self.prompt_bank: Dict[str, List[str]] = self._build_prompt_bank(self.categories)

        # === PROBE PROMPTS for targeted post-checks ===
        self.probe_bank: Dict[str, List[str]] = self._build_probe_bank()

        # === Precompute text feature centroids (avg over prompts) per model ===
        self.text_features_by_model: List[torch.Tensor] = []
        self.probe_features_by_model: List[Dict[str, torch.Tensor]] = []
        for m_idx, model in enumerate(self.models):
            txt_feats = self._encode_prompt_bank_for_model(model, self.prompt_bank)
            self.text_features_by_model.append(txt_feats)  # (num_classes, d)

            probe_feats = self._encode_probe_bank_for_model(model, self.probe_bank)
            self.probe_features_by_model.append(probe_feats)

        print(f"Initialized CLIP (multi-prompt) ensemble with {len(self.model_names)} model(s) "
              f"and {len(self.category_names)} categories")

    # -------------------------------------------------------------------------
    # Prompt construction (kept as in your current version)
    # -------------------------------------------------------------------------
    def _build_prompt_bank(self, base_desc: Dict[str, str]) -> Dict[str, List[str]]:
        """Create multiple visual, contrastive prompts per category."""
        pb = {}

        def add(cat, prompts):
            # Ensure category description is included as first prompt
            if cat in base_desc:
                prompts = [base_desc[cat]] + prompts
            pb[cat] = prompts

        add("HMI DISPLAY LAYOUTS", [
            "A full digital instrument cluster dashboard UI showing gauges like speedometer and tachometer.",
            "A wide automotive dashboard screen with multiple regions and indicators visible together.",
            "A complete cockpit display layout, not a single isolated icon.",
            "Multiple gauges and UI elements on one screen; not a lone warning symbol.",
            "Digital cluster layout with speed, RPM, and fuel; not one icon on plain background."
        ])

        add("CONFIGURATION TABLES", [
            "A spreadsheet-style table with rows and columns where every cell is text or numbers only.",
            "A configuration matrix with letters, digits, units, and values; no pictograms in any cell.",
            "A technical table with headers and borders; cells contain text-only content.",
            "A dense grid of alphanumeric entries; no small drawings or silhouettes.",
            "A text-only table; not a table with icons."
        ])

        add("MULTI-CONDITION LOGIC", [
            "A Boolean logic diagram with AND and OR gate symbols connected by lines.",
            "Condition rectangles feeding into logic gates that combine the inputs.",
            "Gate icons (AND, OR) producing an output chain; not a module block diagram.",
            "A logic schematic where multiple signals are combined with AND/OR gates.",
            "Boolean expressions represented with gate symbols rather than component boxes.",
        ])

        add("SYSTEM ARCHITECTURE DIAGRAMS", [
            "A system block diagram with rectangular modules connected by arrows showing data or wiring.",
            "ECUs, controllers, sensors as boxes with named connections between modules.",
            "Component boxes and connectors; no Boolean logic gate symbols.",
            "A high-level architecture drawing of subsystems and data flow.",
        ])

        add("STATE FLOW DIAGRAMS", [
            "A state machine with circular or oval states connected by transition arrows.",
            "Contains start/end states and labeled transitions.",
            "State bubbles with arrows; not a table or waveform.",
            "Sequential state changes with conditions on edges."
        ])

        add("FLOWCHART DIAGRAMS", [
            "NOT digital waveform chart with clock-like edges, boolean states, and labelled signal rows.",
            "A process flowchart with rectangles for steps and diamonds for decisions.",
            "Arrows connect shapes to show workflow and branching.",
            "A flowchart with decision diamonds labeled Yes and No.",
            "Start and End terminators lead a sequential procedure.",
            "A procedural diagram of steps and decisions",
        ])

        add("TECHNICAL SPECIFICATIONS", [
            "A document page with paragraphs, bullet lists, or section headings; text-dominant.",
            "Technical sheet without arrows or decision diamonds; no workflow.",
            "Specification content in text blocks or small tables; not a dense spreadsheet grid.",
            "Text-heavy layout; no pictograms or dashboard icons."
        ])

        add("WIRING &amp; SIGNAL DIAGRAMS", [
            "An electrical schematic showing wires, connectors, pins, and circuit symbols.",
            "Electrical wiring diagram with nets and pin labels.",
            "Circuit-like line connections; not a table and not a waveform plot."
        ])

        add("TIMING DIAGRAMS", [
            "A digital timing diagram with a horizontal time axis labeled 't' and multiple stacked waveform rows.",
            "Rectangular HIGH/LOW digital waveforms with sharp step transitions and long flat logic levels.",
            "Multiple parallel signal traces aligned vertically, each showing state changes over time.",
            "Vertical dashed reference lines marking synchronization points or phase boundaries.",
            "Time‑based diagram showing signal transitions, activation conditions, and timing relationships.",
            "Rows of digital states progressing left‑to‑right in time, not flowchart boxes or circuit wiring.",
            "Oscillating or stepped logic signals arranged in a grid-like timing chart with temporal alignment.",
            "Digital waveform chart with clock-like edges, boolean states, and labelled signal rows.",
            "Diagram emphasizing chronological progression and signal behavior, not modules, connectors, or arrows between boxes."
        ])

        add("TIMING – ANALOG / THRESHOLD", [
            "An analog plot with a single ramp or slope versus a labeled axis with units.",
            "A signal profile over time with dashed guide lines and reference markers.",
            "A threshold chart showing ON and OFF versus a parameter on the x‑axis with units.",
            "A state versus speed plot with vertical markers at setpoints like V_LIM and V_LIM − 5.",
            "A continuous trace within axes; focus on values and thresholds, not stacked digital bars."
        ])
        add("TABLE WITH TELLTALES", [
            "A table that contains automotive warning icons or pictograms inside its cells.",
            "Grid cells include battery icon, oil lamp, ABS, seatbelt, airbag, brake, or triangle warning.",
            "A table with graphical symbols (not text) embedded in one or more cells.",
            "Not a text-only table; at least one cell contains a warning pictogram."
        ])

        add("COLOR AND GRADIENTS", [
            "Color charts, swatches, or gradient bars used for calibration.",
            "Rainbow gradient scales or color palettes; no text.",
            "Pure color patterns without icons."
        ])

        add("TELLTALE ICONS AND INDICATORS", [
            "A single isolated automotive warning icon on a plain background.",
            "One dashboard pictogram such as battery, oil, check engine, ABS, or seatbelt.",
            "Single icon; no gauges, no tables, no text."
        ])

        add("OTHERS", [
            "An image that does not match any of the defined categories above."
        ])

        return pb

    def _build_probe_bank(self) -> Dict[str, List[str]]:
        """Attribute probes to fix common confusions (unchanged)."""
        return {
            # For HMI vs single icon confusion
            "ICON_PICTOGRAM": [
                "An automotive warning icon or dashboard pictogram.",
                "A car warning symbol such as battery, oil lamp, ABS, or seatbelt.",
                "A small isolated pictogram icon; not text."
            ],
            "HMI_DISPLAY": [
                "A full instrument cluster dashboard UI with multiple gauges on one screen.",
                "A digital cockpit display with speedometer and tachometer together.",
                "A wide dashboard layout with multiple regions and indicators."
            ],
            # For flowchart vs technical specs confusion
            # (You didn't define 'FLOWCHART' probe; we use 'FLOWCHART_PROCESS' where needed.)
            "TECH_TEXT": [
                "A technical document page with text, lists, and parameter tables; no arrows.",
                "Text-heavy specification or measurement sheet without decision diamonds.",
                "A specification table or list; not a flowchart."
            ],
            # For color/gradient vs technical specs confusion
            "COLOR_GRADIENT": [
                "A color chart with swatches or a gradient bar for calibration.",
                "A rainbow gradient scale or color palette without text.",
                "Pure color patterns and gradients."
            ],
            # For table-with-telltales guard vs configuration tables
            "TEXT_ONLY_TABLE": [
                "A spreadsheet-like table made of rows and columns containing only text and numbers.",
                "A parameter matrix with text-only cells; no pictograms or warning symbols.",
                "A configuration table with letters and digits only; no icons in cells."
            ],
            # Extend your existing probe bank with:
            "TIMING_WAVEFORM": [
                "A timing diagram with stacked digital signals showing HIGH and LOW waveforms.",
                "Step-like rectangular waveforms with signal edges and time axis.",
                "Multiple signal traces aligned to a horizontal time axis with temporal relationships.",
                "Digital waveforms with clock edges and data transitions over time."
            ],
            "TANALOG_THRESH_CUES": [
                "An analog single or few traces within axes with units, such as a ramp over time.",
                "A state versus parameter chart with ON and OFF against a non-time x-axis like km/h or °C.",
                "Threshold markers or arrows at setpoints such as V_LIM and V_LIM − 5.",
            ],
            "FLOWCHART_PROCESS": [
                "A flowchart with decision diamonds and Yes/No branches.",
                "Start and End terminators in a process workflow.",
                "A sequential chain of process rectangles connected by arrows.",
                "Process steps and decision logic with workflow arrows."
            ],
        }

    # -------------------------------------------------------------------------
    # Image heuristics for black-background (NEW)
    # -------------------------------------------------------------------------
    def _dark_background_ratio(self, pil_image: Image.Image, thr: int = None) -> float:
        """
        Share of pixels darker than `thr` (0..255) in grayscale. Returns value in [0,1].
        """
        if thr is None:
            thr = self.dark_pixel_thr
        g = np.array(pil_image.convert("L"), dtype=np.uint8)
        return float((g < thr).mean())

    def _edge_density(self, pil_image: Image.Image) -> float:
        """
        Simple texture proxy: fraction of 'strong edge' pixels.
        HMI (UI glyphs) ~ higher; Telltale (single symbol) ~ very low.
        """
        edges = np.array(pil_image.convert("L").filter(ImageFilter.FIND_EDGES), dtype=np.uint8)
        return float((edges > 64).mean())

    # -------------------------------------------------------------------------
    # Text encoding per model (multi-prompt -> centroid per category)
    # -------------------------------------------------------------------------
    def _encode_prompt_bank_for_model(self, model, prompt_bank: Dict[str, List[str]]) -> torch.Tensor:
        """Return (num_classes, d) text centroids for a model."""
        centroids = []
        for cat in self.category_names:
            prompts = prompt_bank[cat]
            text_tokens = clip.tokenize(prompts).to(self.device)
            with torch.no_grad():
                if self.device == "cuda":
                    text_features = model.encode_text(text_tokens).half()
                else:
                    text_features = model.encode_text(text_tokens)
                text_features = _l2_normalize(text_features, dim=-1)
                centroid = text_features.mean(dim=0)
                centroid = _l2_normalize(centroid, dim=-1)
            centroids.append(centroid)
        return torch.stack(centroids, dim=0)  # (num_classes, d)

    def _encode_probe_bank_for_model(self, model, probe_bank: Dict[str, List[str]]) -> Dict[str, torch.Tensor]:
        """Return dict[name] -> (d,) probe centroid features for a model."""
        out = {}
        for name, prompts in probe_bank.items():
            text_tokens = clip.tokenize(prompts).to(self.device)
            with torch.no_grad():
                if self.device == "cuda":
                    feats = model.encode_text(text_tokens).half()
                else:
                    feats = model.encode_text(text_tokens)
                feats = _l2_normalize(feats, dim=-1)
                centroid = _l2_normalize(feats.mean(dim=0), dim=-1)
            out[name] = centroid
        return out

    # -------------------------------------------------------------------------
    # Image encoding + scoring
    # -------------------------------------------------------------------------
    def _encode_image_for_model(self, model, preprocess, pil_image: Image.Image) -> torch.Tensor:
        img = preprocess(pil_image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            if self.device == "cuda":
                img = img.half()
                img_feat = model.encode_image(img).half()
            else:
                img_feat = model.encode_image(img)
            img_feat = _l2_normalize(img_feat, dim=-1)  # (1, d)
        return img_feat.squeeze(0)  # (d,)

    def _logits_for_model(self, model_idx: int, pil_image: Image.Image) -> torch.Tensor:
        """Similarity logits for one model against all categories."""
        model = self.models[model_idx]
        preprocess = self.preprocess_fns[model_idx]
        text_feats = self.text_features_by_model[model_idx]  # (C, d)

        img_feat = self._encode_image_for_model(model, preprocess, pil_image)  # (d,)
        # Use model's logit scale if available; fallback to 100.0 like CLIP
        with torch.no_grad():
            try:
                logit_scale = model.logit_scale.exp().item()
            except Exception:
                logit_scale = 100.0
        logits = logit_scale * (img_feat @ text_feats.T)  # (C,)
        if self.temperature != 1.0:
            logits = logits / self.temperature

        return logits  # (C,)

    def _probe_scores_for_model(self, model_idx: int, pil_image: Image.Image) -> Dict[str, float]:
        """Compute probe similarities (cosine scaled) for post-check rules."""
        model = self.models[model_idx]
        preprocess = self.preprocess_fns[model_idx]
        probes = self.probe_features_by_model[model_idx]

        img_feat = self._encode_image_for_model(model, preprocess, pil_image)  # (d,)
        scores = {name: float(img_feat @ feat) for name, feat in probes.items()}
        return scores

    def _ensemble_logits(self, pil_image: Image.Image) -> torch.Tensor:
        logits_accum = None
        for m_idx in range(len(self.models)):
            logits = self._logits_for_model(m_idx, pil_image)  # (C,)
            logits = logits * self.model_weights[m_idx]
            logits_accum = logits if logits_accum is None else (logits_accum + logits)
        return logits_accum  # (C,)

    def _ensemble_probes(self, pil_image: Image.Image) -> Dict[str, float]:
        # Weighted average of probe cosine scores across models
        agg = {}
        for m_idx in range(len(self.models)):
            scores = self._probe_scores_for_model(m_idx, pil_image)
            w = self.model_weights[m_idx]
            for k, v in scores.items():
                agg[k] = agg.get(k, 0.0) + w * v
        return agg  # name -> cosine score

    # -------------------------------------------------------------------------
    # Post-classification rules (with black-background restriction)
    # -------------------------------------------------------------------------
    def _apply_post_checks(
        self,
        pil_image: Image.Image,
        logits: torch.Tensor,
        top_idx: int
    ) -> int:
        """
        Adjust misclassifications using probe scores.
        Returns possibly updated predicted index.
        """
        probs = torch.softmax(logits, dim=-1).detach().cpu().numpy()
        top_prob = float(probs[top_idx])

        probe = self._ensemble_probes(pil_image)

        def softmax_pair(a: float, b: float) -> Tuple[float, float]:
            ab = torch.tensor([a, b], dtype=torch.float32)
            p = torch.softmax(ab, dim=0).numpy().tolist()
            return p[0], p[1]

        def idx(cat: str) -> int:
            return self.category_names.index(cat)

        pred_name = self.category_names[top_idx]

        # === BLACK BACKGROUND RESTRICTION (3-way: HMI / Telltale / Color) ===
        if self.black_bg_enabled:
            dark_ratio = self._dark_background_ratio(pil_image, thr=self.dark_pixel_thr)
            if dark_ratio >= self.dark_bg_threshold:
                hmi_idx   = idx("HMI DISPLAY LAYOUTS")
                icon_idx  = idx("TELLTALE ICONS AND INDICATORS")
                color_idx = idx("COLOR AND GRADIENTS")

                hmi_logit   = float(logits[hmi_idx])
                icon_logit  = float(logits[icon_idx])
                color_logit = float(logits[color_idx])

                tri = [(hmi_logit, hmi_idx), (icon_logit, icon_idx), (color_logit, color_idx)]
                tri.sort(reverse=True, key=lambda x: x[0])
                pick_idx = tri[0][1]
                top_gap  = tri[0][0] - tri[1][0]

                # If logits are close, fall back to probes
                p_hmi   = probe.get("HMI_DISPLAY",    0.0)
                p_icon  = probe.get("ICON_PICTOGRAM", 0.0)
                p_color = probe.get("COLOR_GRADIENT", 0.0)

                if top_gap < self.black_logit_tie:
                    trio = [(p_hmi, hmi_idx), (p_icon, icon_idx), (p_color, color_idx)]
                    trio.sort(reverse=True, key=lambda x: x[0])
                    pick_idx = trio[0][1]

                    # If winner is HMI or Telltale and probes are near‑tied, use edge density
                    if pick_idx in (hmi_idx, icon_idx) and abs(p_hmi - p_icon) < 0.02:
                        ed = self._edge_density(pil_image)
                        pick_idx = hmi_idx if ed >= self.edge_density_tie else icon_idx

                # Strong override toward Color if its probe clearly dominates
                if (p_color - max(p_hmi, p_icon)) >= self.black_probe_strong:
                    pick_idx = color_idx

                return pick_idx
        # === END black background restriction ===

        # 1) HMI DISPLAY LAYOUTS misclassified as TELLTALE ICONS
        if pred_name == "TELLTALE ICONS AND INDICATORS":
            p_icon, p_hmi = softmax_pair(probe.get("ICON_PICTOGRAM", 0.0), probe.get("HMI_DISPLAY", 0.0))
            if (p_hmi - p_icon) >= 0.15 and top_prob < 0.95:
                return idx("HMI DISPLAY LAYOUTS")

        # TABLE WITH TELLTALES predicted but icon evidence weak -> CONFIGURATION TABLES
        if pred_name == "TABLE WITH TELLTALES":
            p_icon, p_textonly = softmax_pair(probe.get("ICON_PICTOGRAM", 0.0), probe.get("TEXT_ONLY_TABLE", 0.0))
            if (p_textonly - p_icon) >= 0.10 and top_prob < 0.98:
                return idx("CONFIGURATION TABLES")

        # 2) FLOWCHART misclassified as TECHNICAL SPECIFICATIONS
        #    BUG FIX: use FLOWCHART_PROCESS (you don't define 'FLOWCHART')
        if pred_name == "TECHNICAL SPECIFICATIONS":
            p_flow, p_tech = softmax_pair(probe.get("FLOWCHART_PROCESS", 0.0), probe.get("TECH_TEXT", 0.0))
            if (p_flow - p_tech) >= 0.10 and top_prob < 0.98:
                return idx("FLOWCHART DIAGRAMS")

        # 3) COLOR AND GRADIENTS swapped with TECHNICAL SPECIFICATIONS
        if pred_name == "TECHNICAL SPECIFICATIONS":
            p_color, p_tech = softmax_pair(probe.get("COLOR_GRADIENT", 0.0), probe.get("TECH_TEXT", 0.0))
            if (p_color - p_tech) >= 0.12 and top_prob < 0.98:
                return idx("COLOR AND GRADIENTS")

        if pred_name == "COLOR AND GRADIENTS":
            p_color, p_tech = softmax_pair(probe.get("COLOR_GRADIENT", 0.0), probe.get("TECH_TEXT", 0.0))
            if (p_tech - p_color) >= 0.12 and top_prob < 0.98:
                return idx("TECHNICAL SPECIFICATIONS")

        # 4) TIMING DIAGRAMS vs FLOWCHART DIAGRAMS confusion
        if pred_name == "FLOWCHART DIAGRAMS":
            p_timing, p_flow = softmax_pair(probe.get("TIMING_WAVEFORM", 0.0), probe.get("FLOWCHART_PROCESS", 0.0))
            if (p_timing - p_flow) >= 0.12 and top_prob < 0.95:
                return idx("TIMING DIAGRAMS")

        if pred_name == "TIMING DIAGRAMS":
            p_timing, p_flow = softmax_pair(probe.get("TIMING_WAVEFORM", 0.0), probe.get("FLOWCHART_PROCESS", 0.0))
            if (p_flow - p_timing) >= 0.12 and top_prob < 0.95:
                return idx("FLOWCHART DIAGRAMS")

        return top_idx

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------
    def classify_image(self, image_path: str) -> Tuple[str, str, str]:
        """
        Classify a single image using CLIP multi-prompt ensemble classification
        + targeted post-checks.

        Returns: (category, confidence_label, description)
        """
        try:
            image = Image.open(image_path).convert('RGB')

            logits = self._ensemble_logits(image)  # (num_classes,)
            probs = torch.softmax(logits, dim=-1).detach().cpu().numpy()
            best_idx = int(np.argmax(probs))
            best_idx_post = self._apply_post_checks(image, logits, best_idx)

            final_idx = best_idx_post
            category = self.category_names[final_idx]
            confidence_score = float(probs[final_idx])

            # Confidence label
            if confidence_score > 0.7:
                confidence = "High"
            elif confidence_score > 0.4:
                confidence = "Medium"
            else:
                confidence = "Low"

            description = (
                f"CLIP multi-prompt ensemble ({', '.join(self.model_names)}; T={self.temperature}): "
                f"{self.categories[category]} (score: {confidence_score:.3f})"
            )
            return category, confidence, description

        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return "Unknown", "Low", f"Error: {str(e)}"

    def get_category_probabilities(self, image_path: str) -> Dict[str, float]:
        """
        Get probabilities for all categories using the ensemble
        """
        try:
            image = Image.open(image_path).convert('RGB')
            logits = self._ensemble_logits(image)
            probs = torch.softmax(logits, dim=-1).detach().cpu().numpy()
            return dict(zip(self.category_names, probs))
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return {}


def main():
    """
    Example usage of CLIP classifier
    """
    # Initialize classifier
    classifier = CLIPImageClassifier(device="cpu")  # Use "cuda" if GPU available

    # Example 1: Classify single image
    image_path = "static/F834_image13_SystemArchitecture.png"
    if os.path.exists(image_path):
        category, confidence, description = classifier.classify_image(image_path)
        print(f"\nSingle Image Classification:")
        print(f"Image: {image_path}")
        print(f"Category: {category}")
        print(f"Confidence: {confidence}")
        print(f"Description: {description}")

        # Show all probabilities
        probs = classifier.get_category_probabilities(image_path)
        print(f"\nAll Category Probabilities:")
        for cat, prob in sorted(probs.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat}: {prob:.3f}")

    print(f"CLIP classifier ready for use!")


if __name__ == "__main__":
    main()