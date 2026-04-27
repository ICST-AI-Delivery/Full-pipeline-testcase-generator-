import os
import csv
import cv2
import numpy as np
from datetime import datetime
from PIL import Image

# Define unified classification criteria (11 categories)
classification_criteria = {
    "TELLTALE ICONS & INDICATORS": {
        "criteria": "(simple symbols OR indicator icons OR dashboard warning lights)",
        "confidence": lambda symbols: "High" if symbols > 5 else "Medium"
    },
    "CONFIGURATION TABLES": {
        "criteria": "(clear rows AND columns AND headers AND data specifications)",
        "confidence": lambda rows, cols, headers: "High" if rows > 5 and cols > 5 and headers else "Medium"
    },
    "HMI DISPLAY LAYOUTS": {
        "criteria": "(complete interface AND multiple indicators AND instrument cluster OR UI wireframes)",
        "confidence": lambda complete, indicators: "High" if complete and indicators > 10 else "Medium"
    },
    "STATE EVENT MATRICES": {
        "criteria": "(grid pattern AND input/output mapping AND state transitions)",
        "confidence": lambda grid, mapping: "High" if grid and mapping else "Medium"
    },
    "MULTI-CONDITION LOGIC TABLES": {
        "criteria": "(complex table AND conditional relationships AND decision logic)",
        "confidence": lambda complex_table, relationships: "High" if complex_table and relationships else "Medium"
    },
    "SYSTEM ARCHITECTURE DIAGRAMS": {
        "criteria": "(rectangular components AND connection lines AND system design OR data flow)",
        "confidence": lambda components, lines: "High" if components > 10 and lines > 5 else "Medium"
    },
    "PROCESS FLOW DIAGRAMS": {
        "criteria": "(flowchart symbols AND sequential flow AND process steps OR decision trees)",
        "confidence": lambda symbols, flow: "High" if symbols > 5 and flow else "Medium"
    },
    "TECHNICAL SPECIFICATIONS": {
        "criteria": "(explanatory diagrams AND annotations AND parameter documentation)",
        "confidence": lambda diagrams, annotations: "High" if diagrams and annotations else "Medium"
    },
    "WIRING & SIGNAL DIAGRAMS": {
        "criteria": "(electrical connections AND signal routing AND wiring documentation)",
        "confidence": lambda connections, routing: "High" if connections and routing else "Medium"
    },
    "TIMING DIAGRAMS": {
        "criteria": "(horizontal timelines AND signal events AND temporal behavior OR waveforms)",
        "confidence": lambda timelines, events: "High" if timelines and events else "Medium"
    },
    "TABLE + TELLTALES": {
        "criteria": "(structured table AND embedded visual indicators AND telltale symbols)",
        "confidence": lambda table, indicators: "High" if table and indicators > 3 else "Medium"
    }
}

def preprocess_image(image_path, target_size=(224, 224)):
    """
    Preprocess image with enhanced techniques for better classification.
    
    Args:
        image_path (str): Path to the image file
        target_size (tuple): Target size for resizing (width, height)
    
    Returns:
        np.ndarray: Preprocessed image array or None if error
    """
    try:
        # Read image using OpenCV
        image = cv2.imread(image_path)
        if image is None:
            print(f'Warning: Could not read image {image_path}')
            return None
        
        # Resize image to target size
        image = cv2.resize(image, target_size)
        
        # Convert from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Apply contrast enhancement using CLAHE
        lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        image = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        
        # Normalize pixel values to [0, 1]
        image = image.astype(np.float32) / 255.0
        
        # Optional: Apply Gaussian blur for noise reduction
        image = cv2.GaussianBlur(image, (3, 3), 0)
        
        return image
    except Exception as e:
        print(f'Error processing {image_path}: {e}')
        return None

def analyze_image_features(preprocessed_image):
    """
    Extract features from preprocessed image for classification.
    
    Args:
        preprocessed_image (np.ndarray): Preprocessed image array
    
    Returns:
        dict: Dictionary of extracted features
    """
    if preprocessed_image is None:
        return {}
    
    # Convert back to uint8 for feature extraction
    img_uint8 = (preprocessed_image * 255).astype(np.uint8)
    gray = cv2.cvtColor(img_uint8, cv2.COLOR_RGB2GRAY)
    
    features = {}
    
    # Edge detection for structural analysis
    edges = cv2.Canny(gray, 50, 150)
    features['edge_density'] = np.sum(edges > 0) / edges.size
    
    # Line detection for tables and diagrams
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=30, maxLineGap=10)
    features['line_count'] = len(lines) if lines is not None else 0
    
    # Contour analysis for component detection
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    features['contour_count'] = len(contours)
    features['large_contours'] = len([c for c in contours if cv2.contourArea(c) > 100])
    
    # Aspect ratio analysis
    if contours:
        rectangles = 0
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = w / float(h)
                if 0.8 < aspect_ratio < 1.2:  # Roughly square
                    rectangles += 1
        features['rectangular_shapes'] = rectangles
    else:
        features['rectangular_shapes'] = 0
    
    # Text region detection (simplified)
    features['text_regions'] = features['contour_count'] - features['large_contours']
    
    return features

def classify_image(image_path):
    """
    Enhanced image classification using preprocessing and feature analysis.
    
    Args:
        image_path (str): Path to the image file
    
    Returns:
        tuple: (image_type, confidence, visual_characteristics)
    """
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    if preprocessed_image is None:
        return "Unknown", "Low", "Could not process image"
    
    # Extract features
    features = analyze_image_features(preprocessed_image)
    if not features:
        return "Unknown", "Low", "Could not extract features"
    
    # Classification logic based on extracted features (11 unified categories)
    classifications = []
    
    # TELLTALE ICONS & INDICATORS classification (simpler shapes, fewer lines)
    if features['contour_count'] > 3 and features['line_count'] < 15:
        telltale_score = features['contour_count'] * 2
        classifications.append(("TELLTALE ICONS & INDICATORS", telltale_score))
    
    # SYSTEM ARCHITECTURE DIAGRAMS classification
    if features['large_contours'] > 5 and features['line_count'] > 15:
        arch_score = features['large_contours'] * 5 + min(50, features['line_count'])
        classifications.append(("SYSTEM ARCHITECTURE DIAGRAMS", arch_score))
    
    # CONFIGURATION TABLES classification
    if features['line_count'] > 20 and features['rectangular_shapes'] > 10:
        table_score = min(100, features['line_count'] + features['rectangular_shapes'] * 2)
        classifications.append(("CONFIGURATION TABLES", table_score))
    
    # STATE EVENT MATRICES classification
    if features['rectangular_shapes'] > 8 and features['edge_density'] > 0.1:
        matrix_score = features['rectangular_shapes'] * 3 + int(features['edge_density'] * 100)
        classifications.append(("STATE EVENT MATRICES", matrix_score))
    
    # MULTI-CONDITION LOGIC TABLES classification
    if features['rectangular_shapes'] > 10 and features['line_count'] > 15 and features['text_regions'] > 8:
        logic_score = features['rectangular_shapes'] * 2 + features['line_count'] + features['text_regions']
        classifications.append(("MULTI-CONDITION LOGIC TABLES", logic_score))
    
    # PROCESS FLOW DIAGRAMS classification
    if features['contour_count'] > 10 and features['line_count'] > 10:
        workflow_score = features['contour_count'] + features['line_count']
        classifications.append(("PROCESS FLOW DIAGRAMS", workflow_score))
    
    # TIMING DIAGRAMS classification
    if features['line_count'] > 25 and features['edge_density'] > 0.05:
        timing_score = features['line_count'] + int(features['edge_density'] * 200)
        classifications.append(("TIMING DIAGRAMS", timing_score))
    
    # WIRING & SIGNAL DIAGRAMS classification
    if features['line_count'] > 20 and features['edge_density'] > 0.08 and features['large_contours'] < 8:
        wiring_score = features['line_count'] * 2 + int(features['edge_density'] * 150)
        classifications.append(("WIRING & SIGNAL DIAGRAMS", wiring_score))
    
    # HMI DISPLAY LAYOUTS classification (complex interfaces with many elements)
    if features['large_contours'] > 8 and features['text_regions'] > 15 and features['rectangular_shapes'] > 12:
        hmi_score = features['large_contours'] * 3 + features['text_regions'] * 2 + features['rectangular_shapes']
        classifications.append(("HMI DISPLAY LAYOUTS", hmi_score))
    
    # TECHNICAL SPECIFICATIONS classification (text-heavy with structured elements)
    if features['text_regions'] > 15 and features['rectangular_shapes'] > 5:
        tech_score = features['text_regions'] * 2 + features['rectangular_shapes']
        classifications.append(("TECHNICAL SPECIFICATIONS", tech_score))
    
    # TABLE + TELLTALES classification (mixed content)
    if features['rectangular_shapes'] > 8 and features['contour_count'] > 10 and features['line_count'] > 15:
        mixed_score = features['rectangular_shapes'] + features['contour_count'] + features['line_count'] / 2
        classifications.append(("TABLE + TELLTALES", mixed_score))
    
    # Determine best classification
    if not classifications:
        # Fallback classification based on basic features
        if features['text_regions'] > features['large_contours']:
            image_type = "TECHNICAL SPECIFICATIONS"
            confidence = "Low"
        else:
            image_type = "HMI DISPLAY LAYOUTS"
            confidence = "Low"
    else:
        # Sort by score and get the highest
        classifications.sort(key=lambda x: x[1], reverse=True)
        image_type = classifications[0][0]
        score = classifications[0][1]
        
        # Determine confidence based on score
        if score > 80:
            confidence = "High"
        elif score > 40:
            confidence = "Medium"
        else:
            confidence = "Low"
    
    # Generate visual characteristics description
    characteristics_parts = []
    if features['line_count'] > 20:
        characteristics_parts.append("high line density")
    if features['rectangular_shapes'] > 10:
        characteristics_parts.append("multiple rectangular components")
    if features['large_contours'] > 5:
        characteristics_parts.append("distinct structural elements")
    if features['edge_density'] > 0.1:
        characteristics_parts.append("strong edge definition")
    if features['text_regions'] > 10:
        characteristics_parts.append("text regions present")
    
    if not characteristics_parts:
        visual_characteristics = "Basic visual elements detected"
    else:
        visual_characteristics = ", ".join(characteristics_parts)
    
    # Add feature summary to characteristics
    feature_summary = f" | Lines: {features['line_count']}, Shapes: {features['rectangular_shapes']}, Contours: {features['contour_count']}"
    visual_characteristics += feature_summary
    
    return image_type, confidence, visual_characteristics

def update_csv(csv_path, classifications):
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        for classification in classifications:
            writer.writerow(classification)

def main(image_directory, csv_path):
    """
    Main function to process all images in a directory and update CSV with classifications.
    
    Args:
        image_directory (str): Directory containing images to classify
        csv_path (str): Path to CSV file for storing results
    """
    print(f"Starting image classification process for: {image_directory}")
    
    # Ensure CSV file exists with headers if needed
    if not os.path.exists(csv_path):
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Image Path', 'Filename', 'Image Type', 'Confidence', 
                           'Visual Characteristics', 'Timestamp'])
        print(f"Created new CSV file: {csv_path}")
    
    # Collect all image files first
    image_files = []
    for root, dirs, files in os.walk(image_directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(root, file)
                image_files.append((image_path, file))
    
    if not image_files:
        print(f"No image files found in {image_directory}")
        return
    
    total_files = len(image_files)
    print(f"Found {total_files} images to process")
    
    # Process images with progress tracking
    classifications = []
    errors = 0
    
    for idx, (image_path, file) in enumerate(image_files, 1):
        try:
            print(f"Processing image {idx}/{total_files}: {file}")
            image_type, confidence, visual_characteristics = classify_image(image_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            classifications.append([os.path.relpath(image_path, image_directory), file, image_type, confidence, visual_characteristics, timestamp])
            
            # Update CSV in batches of 10 to avoid losing all data in case of error
            if len(classifications) >= 10:
                update_csv(csv_path, classifications)
                classifications = []
                
        except Exception as e:
            print(f"Error processing {file}: {e}")
            errors += 1
    
    # Save any remaining classifications
    if classifications:
        update_csv(csv_path, classifications)
    
    print(f"\nClassification complete!")
    print(f"Total images processed: {total_files}")
    print(f"Successful: {total_files - errors}, Errors: {errors}")
    print(f"Results saved to: {csv_path}")

if __name__ == "__main__":
    image_directory = "SRS FPI export/SRS_Instrument Cluster"
    csv_path = "image_classifications.csv"
    main(image_directory, csv_path)
