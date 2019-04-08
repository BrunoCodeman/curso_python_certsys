#algo usando requests
#leitura de parâmetros através de sys.argv no ifmain
import sys
import json
import requests

log_file_path = "/var/log/apt/history.log"

__CONFIG__ = json.load(open("configs.json","r"))


def get_weather_from_city(city, country):
    """
    gets weather from the given city of a specific country
    """
    with open("weather_content.json","w") as f:
        key = __CONFIG__["weather_api_key"]
        base_url = __CONFIG__["base_url"]
        url = f"{base_url}/data/2.5/weather?q={city},{country}&APPID={key}"
        res = requests.get(url)
        f.write(res.text)


if __name__ == "__main__":
    get_weather_from_city(sys.argv[1], sys.argv[2])
    
    

