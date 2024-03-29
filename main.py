""" Get AQI from waqi.info by city name """
import json

import requests

import config

TOKEN = config.DEFAULT_CONFIG["API_TOKEN"]
CITY = config.DEFAULT_CONFIG["CITY"]


def get_aqi(city, token) -> int:
    """ Get AQI by City name """
    response = requests.get(
        f"http://api.waqi.info/feed/{city}/?token={token}", timeout=5
    )

    json_data = json.loads(response.text)
    aqi = json_data["data"]["aqi"]
    return aqi


def main():
    """ Main function """
    print(get_aqi(city=CITY, token=TOKEN))


if __name__ == "__main__":
    main()
