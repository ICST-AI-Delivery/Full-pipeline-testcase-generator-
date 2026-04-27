"""
Environment Variable Management Utility
Handles loading and validation of environment variables for the Picture Analyze Agent
"""

import os
from pathlib import Path
from typing import Dict, List, Optional
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Warning: python-dotenv not installed. Please install with: pip install python-dotenv")
    load_dotenv = None


class EnvironmentManager:
    """Manages environment variables and API key configuration"""
    
    def __init__(self, env_file: Optional[str] = None):
        """
        Initialize the environment manager
        
        Args:
            env_file: Path to .env file (defaults to .env in project root)
        """
        self.project_root = Path(__file__).parent.parent
        self.env_file = env_file or self.project_root / ".env"
        self.env_example = self.project_root / ".env.example"
        
        # Load environment variables
        self._load_environment()
    
    def _load_environment(self):
        """Load environment variables from .env file"""
        if load_dotenv is None:
            print("Warning: python-dotenv not available. Using system environment variables only.")
            return
        
        # Check if .env file exists
        if not self.env_file.exists():
            self._create_env_file_guidance()
            return
        
        # Load the .env file
        load_dotenv(self.env_file)
        print(f"Environment variables loaded from: {self.env_file}")
    
    def _create_env_file_guidance(self):
        """Provide guidance for creating .env file"""
        print(f"\n⚠️  Environment file not found: {self.env_file}")
        
        if self.env_example.exists():
            print(f"📋 Please copy the template and add your API keys:")
            print(f"   cp {self.env_example} {self.env_file}")
            print(f"   # Then edit {self.env_file} with your actual API keys")
        else:
            print(f"📝 Please create {self.env_file} with your API keys:")
            print("   ANTHROPIC_API_KEY=your_anthropic_api_key_here")
        
        print("\n🔒 The .env file is automatically ignored by git for security.")
    
    def get_api_key(self, service: str) -> Optional[str]:
        """
        Get API key for a specific service
        
        Args:
            service: Service name (e.g., 'anthropic', 'openai')
            
        Returns:
            API key string or None if not found
        """
        key_mapping = {
            'anthropic': 'ANTHROPIC_API_KEY',
            'openai': 'OPENAI_API_KEY',
            'google': 'GOOGLE_API_KEY',
            'azure': 'AZURE_API_KEY'
        }
        
        env_var = key_mapping.get(service.lower())
        if not env_var:
            raise ValueError(f"Unknown service: {service}")
        
        return os.getenv(env_var)
    
    def validate_required_keys(self, required_services: List[str]) -> Dict[str, str]:
        """
        Validate that all required API keys are present
        
        Args:
            required_services: List of required services (e.g., ['anthropic'])
            
        Returns:
            Dictionary of service -> API key mappings
            
        Raises:
            ValueError: If any required keys are missing
        """
        missing_keys = []
        api_keys = {}
        
        for service in required_services:
            api_key = self.get_api_key(service)
            if not api_key:
                missing_keys.append(service.upper())
            else:
                api_keys[service] = api_key
        
        if missing_keys:
            print(f"\n❌ Missing required API keys: {', '.join(missing_keys)}")
            self._create_env_file_guidance()
            raise ValueError(f"Missing required API keys: {missing_keys}")
        
        return api_keys
    
    def get_config_value(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Get configuration value from environment
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Configuration value or default
        """
        value = os.getenv(key, default)
        if value and key.endswith('_API_KEY'):
            # Clean API keys of problematic characters
            value = value.strip().replace('\xa0', '').replace('\u00a0', '')
        return value
    
    def get_api_config(self) -> Dict[str, any]:
        """
        Get API configuration settings
        
        Returns:
            Dictionary with API configuration
        """
        return {
            'timeout': int(self.get_config_value('API_TIMEOUT', '60')),
            'max_retries': int(self.get_config_value('API_MAX_RETRIES', '3')),
        }


# Global instance for easy access
env_manager = EnvironmentManager()


def get_anthropic_api_key() -> str:
    """
    Convenience function to get Anthropic API key
    
    Returns:
        Anthropic API key
        
    Raises:
        ValueError: If API key is not configured
    """
    keys = env_manager.validate_required_keys(['anthropic'])
    return keys['anthropic']


def get_openai_api_key() -> str:
    """
    Convenience function to get OpenAI API key
    
    Returns:
        OpenAI API key
        
    Raises:
        ValueError: If API key is not configured
    """
    keys = env_manager.validate_required_keys(['openai'])
    return keys['openai']


def validate_environment(required_services: List[str] = None) -> bool:
    """
    Validate that the environment is properly configured
    
    Args:
        required_services: List of required services (defaults to ['anthropic'])
        
    Returns:
        True if environment is valid, False otherwise
    """
    if required_services is None:
        required_services = ['anthropic']
    
    try:
        env_manager.validate_required_keys(required_services)
        print("✅ Environment validation successful")
        return True
    except ValueError as e:
        print(f"❌ Environment validation failed: {e}")
        return False


if __name__ == "__main__":
    """Test the environment manager"""
    print("🔧 Testing Environment Manager")
    print("=" * 50)
    
    # Test basic functionality
    try:
        # Test Anthropic API key
        api_key = get_anthropic_api_key()
        print(f"✅ Anthropic API key loaded: {api_key[:10]}...")
        
        # Test configuration
        config = env_manager.get_api_config()
        print(f"✅ API configuration: {config}")
        
        print("\n🎉 Environment manager is working correctly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
