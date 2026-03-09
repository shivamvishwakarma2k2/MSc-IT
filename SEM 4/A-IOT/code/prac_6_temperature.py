# dht22_monitor.py

import time
import RPi.GPIO as GPIO

# -------------------- GPIO Setup --------------------
GPIO.setmode(GPIO.BCM)

PIN = 4                      # DHT22 Data Pin
MIN_T, MAX_T = 20, 30        # Temperature range (°C)
MIN_H, MAX_H = 30, 70        # Humidity range (%)


# -------------------- Read DHT22 --------------------
def read_dht(pin):
    data = []

    # Send start signal
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.00002)

    # Switch to input mode
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Wait for sensor response
    while GPIO.input(pin):
        pass

    # Read 85 timings
    for _ in range(85):
        count = 0
        while GPIO.input(pin) == GPIO.LOW:
            count += 1
            if count > 100:
                break
        data.append(count)

    # Check valid data
    if len(data) < 40:
        return None, None

    # Convert bits to values
    humidity = sum(data[i] << (7 - i) for i in range(8)) / 10
    temperature = sum(data[16 + i] << (7 - i) for i in range(8)) / 10

    return humidity, temperature


# -------------------- Main Loop --------------------
try:
    while True:

        h, t = read_dht(PIN)

        if h is not None and t is not None:

            print(f"Temperature: {t:.2f} °C")
            print(f"Humidity: {h:.2f} %")

            # Temperature Check
            if t < MIN_T:
                print("Temperature LOW")
            elif t > MAX_T:
                print("Temperature HIGH")
            else:
                print("Temperature Normal")

            # Humidity Check
            if h < MIN_H:
                print("Humidity LOW")
            elif h > MAX_H:
                print("Humidity HIGH")
            else:
                print("Humidity Normal")

            print("-" * 30)

        else:
            print("Sensor Error")

        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()