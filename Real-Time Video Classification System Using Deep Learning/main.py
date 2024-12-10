# main.py
import yaml
import logging
import argparse
from pathlib import Path
from model_loader import load_classes, load_model
from video_processor import process_video

def initialize_logging(log_dir, log_file):
    """Set up logging with the specified directory and file."""
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_dir / log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Argument parser for configuration file path
parser = argparse.ArgumentParser(description="Video Processing Project with Configurable Settings")
parser.add_argument("--config", default="config.yaml", help="Path to the configuration file")
args = parser.parse_args()

# Load configuration from YAML file
config_path = Path(args.config)
if not config_path.is_file():
    print(f"Configuration file not found at {config_path}. Please check the path.")
    exit()

with open(config_path) as f:
    config = yaml.safe_load(f)

# Initialize logging
log_dir = Path(config.get('logging', {}).get('log_directory', 'logs'))
log_file = config.get('logging', {}).get('log_file', 'app.log')
initialize_logging(log_dir, log_file)

# Log the start of the process
logging.info("Starting video processing application")

# Extract paths and settings from configuration
try:
    paths = config['paths']
    classes_file = Path(paths['classes_file'])
    proto_path = Path(paths['proto_path'])
    model_path = Path(paths['model_path'])
    video_path = Path(paths['video_path'])
    settings = config['settings']
except KeyError as e:
    logging.error(f"Configuration key missing: {e}")
    print(f"Error: Missing configuration key: {e}")
    exit()

# Load model and classes
classes = load_classes(classes_file)
net = load_model(proto_path, model_path)

# Process the video with the loaded model and classes
process_video(video_path, net, classes, settings)

# Log the completion of the process
logging.info("Video processing completed successfully")
