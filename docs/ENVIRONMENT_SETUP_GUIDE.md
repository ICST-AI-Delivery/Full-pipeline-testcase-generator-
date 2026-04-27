# Environment Setup Guide

This guide explains how to set up the environment variables and dependencies for the Picture Analyze Agent project.

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Access to required API services (HARMAN, Anthropic, etc.)

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd "Picture Analyze Agent"
```

## Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- `python-dotenv` - For environment variable management
- `litellm` - For API calls to various LLM providers
- `anthropic` - For Anthropic Claude API
- Other dependencies as listed in requirements.txt

## Step 3: Environment Variables Setup

### Create .env File

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your actual API keys:
   ```bash
   # Open .env file in your preferred editor
   notepad .env  # Windows
   nano .env     # Linux/Mac
   ```

### Required API Keys

#### HARMAN_API_KEY
- **Purpose**: Used for HARMAN's internal LLM API access
- **Used by**: 
  - `scripts/automated_vision_pipeline.py`
  - `scripts/generate_consolidated_analysis.py`
  - `scripts/test_single_image.py`
  - `scripts/test_api.py`
- **Format**: `HARMAN_API_KEY=sk-xxxxxxxxxxxxxxxxxx`

#### ANTHROPIC_API_KEY
- **Purpose**: Used for Claude API access in SRS analysis generation
- **Used by**: 
  - `scripts/generate_srs_analysis.py`
- **Format**: `ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxx`

#### Optional API Keys
- `OPENAI_API_KEY`: For future OpenAI integrations
- `GOOGLE_API_KEY`: For future Google AI integrations
- `AZURE_API_KEY`: For future Azure AI integrations

### Example .env File

```env
# Picture Analyze Agent - Environment Variables
# Copy this file to .env and fill in your actual API keys

# Anthropic API Configuration
ANTHROPIC_API_KEY=sk-ant-your_anthropic_api_key_here

# HARMAN API Configuration
HARMAN_API_KEY=sk-your_harman_api_key_here

# OpenAI API Configuration (if used in future)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: API Configuration
API_TIMEOUT=60
API_MAX_RETRIES=3
```

## Step 4: Verify Setup

### Test Environment Loading

Run the environment test script:

```bash
python scripts/test_api.py
```

This will verify that:
- Environment variables are loaded correctly
- API keys are accessible
- Basic API connectivity works

### Test Individual Components

1. **Test Vision API Pipeline**:
   ```bash
   python scripts/automated_vision_pipeline.py --feature VEH-F165_Manettino --category CONFIGURATION_TABLES
   ```

2. **Test Consolidated Analysis**:
   ```bash
   python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
   ```

3. **Test SRS Analysis Generation**:
   ```bash
   python scripts/generate_srs_analysis.py --phase 1 --feature VEH-F165_Manettino
   ```

## Security Best Practices

### .env File Security

1. **Never commit .env files**: The `.gitignore` file is configured to exclude `.env` files
2. **Use strong API keys**: Ensure your API keys are from official sources
3. **Rotate keys regularly**: Update API keys periodically for security
4. **Limit key permissions**: Use API keys with minimal required permissions

### File Permissions

On Unix-like systems, set appropriate permissions for the .env file:

```bash
chmod 600 .env
```

## Troubleshooting

### Common Issues

#### "API key not found" Error

**Problem**: Scripts report that API keys are not found in environment variables.

**Solutions**:
1. Verify `.env` file exists in the project root
2. Check that API key names match exactly (case-sensitive)
3. Ensure no extra spaces around the `=` sign
4. Restart your terminal/IDE after creating `.env`

#### "Module not found" Error

**Problem**: Python cannot find the `utils.env_manager` module.

**Solutions**:
1. Ensure you're running scripts from the project root directory
2. Verify `utils/__init__.py` exists
3. Check that `utils/env_manager.py` exists

#### API Connection Errors

**Problem**: API calls fail with connection or authentication errors.

**Solutions**:
1. Verify API keys are correct and active
2. Check network connectivity
3. Ensure API endpoints are accessible from your network
4. Verify API key permissions and quotas

### Debug Mode

Enable debug logging by setting environment variables:

```bash
# In .env file
DEBUG=true
LOG_LEVEL=DEBUG
```

### Getting Help

1. Check the project documentation in the `documentation/` folder
2. Review error logs for specific error messages
3. Verify all prerequisites are installed
4. Test with minimal examples first

## Environment Variable Reference

| Variable | Required | Purpose | Default |
|----------|----------|---------|---------|
| `HARMAN_API_KEY` | Yes | HARMAN LLM API access | None |
| `ANTHROPIC_API_KEY` | Yes* | Claude API access | None |
| `OPENAI_API_KEY` | No | OpenAI API access | None |
| `API_TIMEOUT` | No | API request timeout | 60 |
| `API_MAX_RETRIES` | No | Max API retry attempts | 3 |
| `DEBUG` | No | Enable debug logging | false |
| `LOG_LEVEL` | No | Logging level | INFO |

*Required only for SRS analysis generation scripts

## Next Steps

After completing the environment setup:

1. Review the [Complete Pipeline Workflow](COMPLETE_PIPELINE_WORKFLOW.md)
2. Read the [Automated Vision Pipeline Guide](AUTOMATED_VISION_PIPELINE_GUIDE.md)
3. Explore the [SRS Analysis Generator Guide](SRS_ANALYSIS_GENERATOR_GUIDE.md)
4. Check the [Consolidated Analysis Generator Guide](CONSOLIDATED_ANALYSIS_GENERATOR_GUIDE.md)

## Updates and Maintenance

### Updating Dependencies

Periodically update Python packages:

```bash
pip install -r requirements.txt --upgrade
```

### Environment File Updates

When new environment variables are added:

1. Check for updates to `.env.example`
2. Add new variables to your `.env` file
3. Update documentation as needed

### API Key Rotation

When rotating API keys:

1. Generate new keys from the respective API providers
2. Update the `.env` file with new keys
3. Test the setup to ensure everything works
4. Revoke old keys from the API providers
