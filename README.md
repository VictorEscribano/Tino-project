# Raspberry Pi Cat Detection and Water Pump Control

This project involves using a Raspberry Pi with a connected USB camera and a water pump. The Raspberry Pi streams video using Flask at the /cam endpoint and reads commands at the /detection endpoint. A remote computer performs image processing to detect cats using YOLO and a Roboflow dataset. If a cat is detected for more than 5 seconds, the water pump is activated and the /detection value is set to 1 until the cat is no longer detected for 5 seconds. When no cat is detected for more than 5 seconds, the /detection value is set to 0.


https://github.com/VictorEscribano/Tino-project/assets/70441479/22f6a664-adaa-4694-8c57-17f71d606dc9


![esquema](https://github.com/VictorEscribano/Tino-project/assets/70441479/93677cfb-76e6-49df-9709-4e9489f51c19)

## Prerequisites

Before running the project, you need to ensure the following:

- Raspberry Pi with USB camera support (tested on Raspberry Pi 3 and 4)
- Python 3.x installed on the Raspberry Pi
- Required Python packages installed (check `requirements.txt`)

## Getting Started

1. Clone this repository to your Raspberry Pi.

2. Intall requirements
 ```console
pip install -r requirements.txt
 ```

## Raspberry Pi Setup
Connect a USB camera and water pump to the Raspberry Pi.
Clone this repository on the Raspberry Pi.

## Raspberry Pi Execution
Navigate to the project directory on the Raspberry Pi.
Start the Flask app:

```python server.py```

The video stream will be available at http://raspberrypi_ip:5000/cam, and the /detection endpoint will be used to control the water pump.

## Remote Computer Setup
Clone this repository on the remote computer.
### Remote Computer Execution
Navigate to the project directory on the remote computer.

```python client.py```

The image processing server will read the video stream from the /cam endpoint on the Raspberry Pi, detect cats using YOLO, and control the water pump accordingly by setting the /detection value on the Raspberry Pi.
