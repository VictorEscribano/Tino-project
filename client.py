#Encargado de procesar la imagen, procesarla y enviarla al servidor
import requests
import cv2
import numpy as np
import time

# Function to perform cat detection on a frame
def detect_cats(frame):
    # Perform cat detection using YOLO and the Roboflow dataset
    # Replace this with your own code to perform cat detection
    # The output should be a boolean indicating whether a cat is detected or not
    return False

# Function to update the /detection endpoint
def update_detection_status(status):
    # Update the /detection endpoint by sending a POST request
    detection_endpoint = 'http://raspberrypi_ip:5000/detection'  # Replace with your Raspberry Pi's IP address
    payload = {'value': status}
    requests.post(detection_endpoint, data=payload)

# Main loop to read frames from the /cam endpoint and perform cat detection
def process_video_stream():
    cat_detected = False
    last_detection_time = time.time()

    # Continuously read frames from the /cam endpoint
    video_stream_url = 'http://raspberrypi_ip:5000/cam'  # Replace with your Raspberry Pi's IP address
    stream = requests.get(video_stream_url, stream=True)

    for chunk in stream.iter_content(chunk_size=4096):
        if chunk:
            # Process the video frame
            frame = np.frombuffer(chunk, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            # Perform cat detection
            cat_detected = detect_cats(frame)

            if cat_detected:
                # Update the last detection time if a cat is detected
                last_detection_time = time.time()
                if not cat_detected:
                    update_detection_status(1)  # Activate the water pump
            elif time.time() - last_detection_time >= 5:
                # Deactivate the water pump if no cat is detected for more than 5 seconds
                if cat_detected:
                    update_detection_status(0)  # Deactivate the water pump

            # Display the frame with cat detection (optional)
            cv2.imshow('Frame', frame)
            cv2.waitKey(1)

# Start processing the video stream
if __name__ == '__main__':
    process_video_stream()
