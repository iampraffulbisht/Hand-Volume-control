![1*oeYqmGm-jf9lZv2nNZSfjQ](https://github.com/iampraffulbisht/Hand-Volume-control/assets/114369813/ff8bb7e2-8efa-476e-9621-482381628fd2)

# Hand Gesture Volume Control

This project allows you to control the system volume using hand gestures captured through a webcam. The project leverages OpenCV for video capture, MediaPipe for hand tracking, and PyCaw for controlling the system audio.

## Prerequisites

Ensure you have Python 3.6 or higher installed on your system.

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/hand-gesture-volume-control.git](https://github.com/iampraffulbisht/Hand-Volume-control
    cd hand-gesture-volume-control
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Dependencies**

    ```bash
    pip install opencv-python
    pip install mediapipe
    pip install numpy
    pip install comtypes
    pip install pycaw
    ```

4. **Download the `hand_tracking_module.py`**

    Ensure you have the `hand_tracking_module.py` file in your project directory. This module should contain the hand detection logic using MediaPipe.

## Running the Code

Run the script to start the webcam and control the volume using hand gestures.

```bash
python main.py
```

License

This project is licensed under the MIT License.

**Acknowledgements

OpenCV
MediaPipe
PyCaw

