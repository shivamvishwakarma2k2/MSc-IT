# traffic_signal.py

import RPi.GPIO as GPIO
import time

# Define pins
RED = 17 # 11
YELLOW = 27 # 13
GREEN = 22 # 15

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([RED, YELLOW, GREEN], GPIO.OUT)

try:
    while True:

        # RED ON (Stop)
        GPIO.output(RED, 1)
        GPIO.output(YELLOW, 0)
        GPIO.output(GREEN, 0)
        print("RED - STOP")
        time.sleep(5)

        # YELLOW ON (Wait)
        GPIO.output(RED, 0)
        GPIO.output(YELLOW, 1)
        GPIO.output(GREEN, 0)
        print("YELLOW - WAIT")
        time.sleep(2)

        # GREEN ON (Go)
        GPIO.output(RED, 0)
        GPIO.output(YELLOW, 0)
        GPIO.output(GREEN, 1)
        print("GREEN - GO")
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()

