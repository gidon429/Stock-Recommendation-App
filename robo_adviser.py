

api_key = "U67K4D8L98Z5XONE"

from dotenv import load_dotenv
import json
import os
import csv
import datetime
import requests
from IPython import embed

load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

def write_data_to_file(filename="{symbol}.csv", data=[]):
    filepath = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def is_valid_ticker(symbol):
    try:
        float(symbol)
        return True
    except Exception as e:
        return False

def wrong_ticker_format():
    print("That format is not valid for a ticker, please enter the correct ticker symbol in capital letters")
    return

api_key = "U67K4D8L98Z5XONE"


# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

symbol = input("Please enter the ticker you would like to see: ")
    #TODO: capture user input
if is_valid_ticker(symbol) == False:
    wrong_ticker_format()
else

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" + api_key
response = requests.get(request_url)
response_body = json.loads(response.text)

metadata = response_body["Meta Data"]
data = response_body["Time Series (Daily)"]
#write_data_to_file(data)
dates = list(data)
#date_list = int(datetime.date(max(dates)) - int(datetime.timedelta(days=100))
#date_list = [float(datetime.timedelta(base)) - datetime.timedelta(days=x) for x in range(0,100)]
latest_daily_data = data[dates[1]]
latest_hundred_days_data = data[dates[99]]
#> {'1. open': '353.8000',
#> '2. high': '355.5300',
#> '3. low': '350.2100',
#> '4. close': '351.6000',
#> '5. volume': '6921687'}
latest_price = latest_daily_data["4. close"]
latest_price = float(latest_price)
latest_price_usd = "${0:,.2f}".format(latest_price)
highest_price = latest_hundred_days_data["2. high"]
highest_price = float(highest_price)
highest_price_usd = "${0:,.2f}".format(highest_price)
lowest_price = latest_hundred_days_data["3. low"]
lowest_price = float(lowest_price)
lowest_price_usd = "${0:,.2f}".format(lowest_price)
print("Summary")
print("-------------------------------------------------")
print("Ticker: " + symbol)
print("Last refreshed on " + max(dates))
print(f"Latest daily closing price for {symbol} is: {latest_price_usd}")
print(f"The recent average high price over the last 100 trading days was {highest_price_usd}")
print(f"The recent average low price over the last 100 trading days was {lowest_price_usd}")

# see: https://www.alphavantage.co/documentation/#daily
# TODO: assemble the request url to get daily data for the given stock symbol

# TODO: issue a "GET" request to the specified url, and store the response in a variable

# TODO: parse the JSON response

#latest_price_usd = "$100,000.00" # TODO: traverse the nested response data structure to find the latest closing price

#print(f"LATEST DAILY CLOSING PRICE FOR {symbol} IS: {latest_price_usd}")
