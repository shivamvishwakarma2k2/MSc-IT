import requests
import RPi.GPIO as GPIO

TOKEN = "YOUR_BOT_TOKEN_HERE"
URL = f"https://api.telegram.org/bot{TOKEN}/"
RELAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

offset = None

while True:

    res = requests.get(URL + "getUpdates",
                     params={"offset": offset}).json()

    for update in res.get("result", []):

        chat = update["message"]["chat"]["id"]
        msg = update["message"].get("text", "").lower()

        if msg == "/relayon":
            GPIO.output(RELAY, GPIO.LOW)
            reply = "ON"

        elif msg == "/relayoff":
            GPIO.output(RELAY, GPIO.HIGH)
            reply = "OFF"

        else:
            reply = "Invalid"

        requests.get(URL + "sendMessage",
                     params={"chat_id": chat, "text": reply})

        offset = update["update_id"] + 1