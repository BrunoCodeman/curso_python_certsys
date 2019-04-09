import os
import sys
import json
import psutil
import requests


#salve seus arquivos neste diretório 
__path__ = f"{diretorio_do_projeto}/src/"
__CONFIG__ = json.load(open(f"{__path__}configs.json","r"))
apt_log_file_path = "/var/log/apt/history.log"


def get_hardware_use():
    """
    Shows python's hardware consumption and total memory/cpu usage
    """
    
    info = f""" 
                python cpu usage: {python_cpu_usage} %
                cpu usage: {cpu_usage_in_percentage} %
                used memory: {used_memory_in_gb} GB
                available memory: {available_memory_in_gb} GB
            """
    return info


def json_apt_history_info():
    """
    Generates a json file with apt history log. It is saved as json_log.json
    """
    pass
            
            
                

def get_weather_from_city(city, country):
    """
    gets weather from the given city of a specific country
    and saves on a file called 'weather_content.txt'
    """
    pass