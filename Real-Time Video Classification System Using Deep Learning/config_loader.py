# config_loader.py
import yaml
import logging


class ConfigLoader:
    def __init__(self, config_file="config.yaml"):
        self.config = self.load_config(config_file)

    def load_config(self, file_path):
        try:
            with open(file_path) as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logging.error("Configuration file not found.")
            exit()

    def get_path(self, key):
        return self.config.get('paths', {}).get(key, None)

    def get_setting(self, key, default=None):
        return self.config.get('settings', {}).get(key, default)
