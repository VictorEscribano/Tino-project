# Encargado de stream de video y leer comandos

import cv2
import numpy as np
import time
from flask import Flask, Response, request, render_template

app = Flask(__name__)
pump_status = 0  # Initial pump status

# Function to initialize the USB camera
def init_camera():
    camera = cv2.VideoCapture(0)  # Use the correct camera index (usually 0 for the first USB camera)
    return camera

# Function to stream video frames from the USB camera
def stream_video(camera):
    global pump_status

    while True:
        if pump_status == 1:
            # Activate water pump
            # Code to activate the water pump goes here
            print("Water pump activated!")
        else:
            # Deactivate water pump
            # Code to deactivate the water pump goes here
            print("Water pump deactivated!")

        # Capture a video frame from the USB camera
        ret, frame = camera.read()

        # Encode the frame as JPEG and yield it as a response
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html', pump_status=pump_status)

@app.route('/cam')
def video_feed():
    camera = init_camera()
    return Response(stream_video(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detection', methods=['GET', 'POST'])
def detection_status():
    global pump_status
    if request.method == 'POST':
        pump_status = int(request.form['value'])
        print("Detection status:", pump_status)
    return str(pump_status)

if __name__ == '__main__':
    app.run(host='192.168.1.39', port=500)
