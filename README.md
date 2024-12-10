

# Real-Time Video Classification System Using Deep Learning

## Overview
This project implements a real-time video classification system using a pre-trained deep learning model (GoogLeNet) and OpenCV. 
The system processes video frames in real-time, predicts top class probabilities for each frame, and overlays the predictions directly on the video. 
It is designed to demonstrate the integration of machine learning models with practical video analysis applications.

## Features
- **Real-Time Video Processing**: Processes video frames efficiently to ensure minimal delay.
- **Deep Learning Inference**: Utilizes a pre-trained GoogLeNet model for accurate frame classification.
- **Class Overlay**: Displays top class predictions with probabilities on each frame for easy interpretability.
- **Performance Metrics**: Measures and logs inference time per frame for benchmarking.
- **Scalable Framework**: Easily adaptable to other models (e.g., MobileNet, ResNet).

## Technologies Used
- **Python**: Core programming language.
- **OpenCV**: For video capture, frame processing, and real-time display.
- **Caffe**: For loading and running pre-trained deep learning models.
- **NumPy**: For efficient numerical computations.

## How It Works
1. **Video Input**: The system reads a video file or stream using OpenCV.
2. **Frame Processing**: Each frame is preprocessed and fed into the deep learning model.
3. **Model Prediction**: The GoogLeNet model predicts class probabilities for each frame.
4. **Overlay Predictions**: Top predictions are displayed on the video frames in real time.
5. **Output Options**: The processed video can be displayed live or saved as a new file.

## Setup and Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/real-time-video-classification.git
   cd real-time-video-classification
   ```
2. Install required dependencies:
   ```bash
   pip install opencv-python numpy
   ```
   (For full functionality, install Caffe and its Python bindings.)

3. Download the pre-trained GoogLeNet model:
   - [Prototxt file](http://dl.caffe.berkeleyvision.org/bvlc_googlenet.prototxt)
   - [Model file](http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel)

4. Update the paths in the script to point to your video, model, and class files.

## Usage
Run the script with your video file:
```bash
python video_classification.py
```
The processed video will be displayed with predictions overlayed on each frame.

## Future Improvements
- Integrate support for additional deep learning frameworks (e.g., TensorFlow, PyTorch).
- Extend to anomaly detection or object tracking applications.
- Optimize for real-time performance using GPU acceleration.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
