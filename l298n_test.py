import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena = 18
In1 = 23
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
pwm = GPIO.PWM(Ena, 100)
pwm.start(0)

while True:
    GPIO.output(In1, GPIO.HIGH)
    pwm.ChangeDutyCycle(100) #half speed, maximum is 100