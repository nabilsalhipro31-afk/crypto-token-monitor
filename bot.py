import requests
import time

class PriceMonitor:

    def __init__(self):
        self.symbol = "BTCUSDT"
        self.last_price = None

    def get_price(self):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}"
        data = requests.get(url).json()
        return float(data["price"])

    def check(self):
        price = self.get_price()
        print("Price:", price)

        if self.last_price:
            diff = price - self.last_price
            if diff > 50:
                print("Price going up")
            if diff < -50:
                print("Price going down")

        self.last_price = price

    def run(self):
        while True:
            self.check()
            time.sleep(5)

monitor = PriceMonitor()
monitor.run()
