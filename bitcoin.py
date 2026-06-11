import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

if amount <= 0:
    sys.exit("Amount must be greater than 0")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=355d772bdbe9615b23cad6e2af725cc228e59dc8cdba4052925ee0fa898c74f3")
    r = response.json()
    price = float(r["data"]["priceUsd"])
    total = round(price * amount, 4)
    print("$" + format(total, ",.4f"))

except requests.RequestException:
    sys.exit("API request failed")