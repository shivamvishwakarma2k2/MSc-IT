import requests
import RPi.GPIO as GPIO

# Telegram Bot Token
TOKEN = "YOUR_BOT_TOKEN"
URL = "https://api.telegram.org/bot" + TOKEN + "/"

# LED setup (GPIO27 = Physical Pin 13)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

offset = None

while True:

    # Get messages from Telegram
    data = requests.get(URL + "getUpdates",
                        params={"offset": offset}).json()

    for update in data["result"]:

        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"].lower()

        # LED ON
        if text == "/ledon":
            GPIO.output(27, True)
            requests.get(URL + "sendMessage",
                         params={"chat_id": chat_id, "text": "LED ON"})

        # LED OFF
        if text == "/ledoff":
            GPIO.output(27, False)
            requests.get(URL + "sendMessage",
                         params={"chat_id": chat_id, "text": "LED OFF"})

        offset = update["update_id"] + 1
