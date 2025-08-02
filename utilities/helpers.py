"""
Utility functions for test framework
"""
import os
import yaml
import json
from datetime import datetime
import logging

class ConfigManager:
    """Manages configuration loading and access"""
    
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from YAML file"""
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def get(self, key, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

class LogManager:
    """Manages logging for the test framework"""
    
    @staticmethod
    def setup_logger(name, log_file=None, level=logging.INFO):
        """Setup logger with file and console handlers"""
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        if not logger.handlers:
            # Console handler
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)
            
            # File handler
            if log_file:
                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                file_handler = logging.FileHandler(log_file)
                file_formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
                )
                file_handler.setFormatter(file_formatter)
                logger.addHandler(file_handler)
        
        return logger

class TestDataManager:
    """Manages test data loading and access"""
    
    @staticmethod
    def load_json_data(file_path):
        """Load test data from JSON file"""
        with open(file_path, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def load_yaml_data(file_path):
        """Load test data from YAML file"""
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

class ReportManager:
    """Manages test reporting utilities"""
    
    @staticmethod
    def generate_timestamp():
        """Generate timestamp for reports"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def create_report_directory(base_dir="reports"):
        """Create report directory with timestamp"""
        timestamp = ReportManager.generate_timestamp()
        report_dir = os.path.join(base_dir, f"test_run_{timestamp}")
        os.makedirs(report_dir, exist_ok=True)
        return report_dir

class ScreenshotManager:
    """Manages screenshot utilities"""
    
    @staticmethod
    def create_screenshot_directory(base_dir="screenshots"):
        """Create screenshot directory"""
        os.makedirs(base_dir, exist_ok=True)
        return base_dir
    
    @staticmethod
    def get_screenshot_path(test_name, timestamp=None):
        """Get screenshot path for a test"""
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = ScreenshotManager.create_screenshot_directory()
        return os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
