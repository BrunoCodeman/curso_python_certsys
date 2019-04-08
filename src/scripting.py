#algo usando requests
#leitura de parâmetros através de sys.argv no ifmain
import os
import sys
import json
import subprocess
import psutil
import requests

log_file_path = "/var/log/apt/history.log"

__CONFIG__ = json.load(open("configs.json","r"))

def get_hardware_use():
    """
    Shows python's hardware consumption and total memory/cpu usage
    """
    pass


def json_apt_history_info():
    """
    Generates a json file with apt history
    """
    pass



def get_weather_from_city(city, country):
    """
    Shows weather from given city from selected country
    """

    pass


if __name__ == "__main__":
    pass
    

