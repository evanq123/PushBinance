import time
import datetime
import sys
import json
try:
    from bs4 import BeautifulSoup
    from pushbullet import PushBullet
    from binance.client import Client
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushBinance \n")
    sys.exit(1)

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

api_key = data["binance_api_key"]
api_secret = data["binance_api_secret"]
client = Client(api_key, api_secret)
push_key = data["push_api_key"]

symbol = input("Enter the symbol: ").upper() + 'BTC'
threshold = float(input("Enter your threshold in BTC: "))
intervals = 5 # Default 5s between checks.

def get_price():
    price = client.get_symbol_ticker(symbol=symbol)["price"]
    print("Price for {} is now: {} BTC".format(symbol, price))
    return price


def push_message(msg):
    pb = PushBullet(push_key)
    pb.push_note("PushBinance: The price for {} has changed!".format(symbol), msg)


message_sent = False # Hackish workaround for now.
def price_past_threshold():
    if float(get_price()) >= float(threshold):
        return True


while True:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if price_past_threshold() and message_sent is False:
        msg = ("As of, {} EST, the price for {} is >= {} BTC (at {})"
               "".format(date, symbol, threshold, get_price()))

        print("Sending message to PushBullet...\n")
        push_message(msg)
        message_sent = True

    if not price_past_threshold() and message_sent is True:
        msg = ("As of, {} EST, the rate for {} is < {} BTC (at {})"
               "".format(date, symbol, threshold, get_price()))
        print("Sending message to PushBullet...\n")
        push_message(msg)
        message_sent = False

    time.sleep(intervals)
