# utils.py
import cv2

def preprocess_frame(frame):
    """Preprocesses the frame to fit the model's input requirements."""
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0, size=(224, 224), mean=(104, 117, 123))
    return blob
