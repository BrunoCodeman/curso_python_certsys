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
    pass

def get_weather_from_city(city, country):
    pass

