import json

import requests

import config

TOKEN = config.DEFAULT_CONFIG["API_TOKEN"]
CITY = config.DEFAULT_CONFIG["CITY"]


def get_aqi(city, token) -> int:
    response = requests.get(
        f"http://api.waqi.info/feed/{city}/?token={token}", timeout=5
    )

    json_data = json.loads(response.text)
    aqi = json_data["data"]["aqi"]
    return print(aqi)


def main():
    get_aqi(city=CITY, token=TOKEN)


if __name__ == "__main__":
    main()
