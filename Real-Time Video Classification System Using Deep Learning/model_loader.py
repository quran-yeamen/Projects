# model_loader.py
import logging
from functools import lru_cache

import cv2
import os


@lru_cache(maxsize=1)
def load_classes(filepath):
    """Loads class labels from a specified file."""
    logging.info(f"Attempting to load class file from {filepath}")
    try:
        with open(filepath) as f:
            classes = [line[line.find(' ') + 1:].strip() for line in f]
        logging.info("Classes loaded successfully.")
        return classes
    except FileNotFoundError:
        logging.error(f"Class file not found at {os.path.abspath(filepath)}. Please check the path.")
        exit()

def load_model(proto_path, model_path):
    """Loads the pre-trained model from specified files."""
    try:
        net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
        logging.info("Model loaded successfully.")
        return net
    except cv2.error:
        logging.error("Model files not found or invalid. Please check the paths.")
        exit()
