import json

import requests

import config

TOKEN = config.DEFAULT_CONFIG["API_TOKEN"]
CITY = config.DEFAULT_CONFIG["CITY"]

response = requests.get(f"http://api.waqi.info/feed/{CITY}/?token={TOKEN}", timeout=10)

json_data = json.loads(response.text)
print(json_data["data"]["aqi"])
