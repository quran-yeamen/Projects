# video_processor.py
import cv2
import time
import numpy as np
import logging
from utils import preprocess_frame
from tqdm import tqdm


def make_predictions(net, classes, frame, confidence_threshold=0.5):
    """Makes predictions on the frame and overlays the top classes with probabilities."""
    blob = preprocess_frame(frame)
    net.setInput(blob)

    outp = net.forward()

    for r, i in enumerate(np.argsort(outp[0])[::-1][:5], start=1):
        confidence = outp[0][i]
        if confidence > confidence_threshold:
            txt = f'{classes[i]}: {confidence * 100:.2f}%'
            cv2.putText(frame, txt, (10, 25 + 40 * r), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)


def process_video(video_path, net, classes, settings):
    """Processes a video file, applying the model on every Nth frame for efficiency, with progress indication."""
    process_every_n_frames = settings.get("process_every_n_frames", 5)
    confidence_threshold = settings.get("confidence_threshold", 0.5)

    # Desired window size
    target_width = 740
    target_height = 460

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        logging.error("Cannot open video stream")
        exit()

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    with tqdm(total=frame_count, desc="Processing video", unit="frame") as pbar:
        frame_number = 0
        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                break

            # Only process every Nth frame
            if frame_number % process_every_n_frames == 0:
                make_predictions(net, classes, frame, confidence_threshold)

            # Resize the frame to the target size
            resized_frame = cv2.resize(frame, (target_width, target_height))

            # Create a named window and set it to resizable mode
            cv2.namedWindow('Processed Frame', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Processed Frame', target_width, target_height)  # Force the window size

            # Display the resized frame with predictions
            cv2.imshow('Processed Frame', resized_frame)

            # Update progress bar
            pbar.update(1)
            frame_number += 1

            # Break on 'ESC' key
            if cv2.waitKey(25) & 0xFF == 27:
                break

    # Release video capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()
