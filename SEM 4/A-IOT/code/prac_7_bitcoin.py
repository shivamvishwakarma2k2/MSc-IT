import requests
import time

API_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def get_bitcoin_price():
	res = requests.get(API_URL)
	return float(res.json()["price"])

if __name__ == "__main__":
	while True:
		try:
			price = get_bitcoin_price()
			print(f"Bitcoin price: {price} $")
			time.sleep(4)
		except Exception as e:
			print(f"Error Occurred: {e}")