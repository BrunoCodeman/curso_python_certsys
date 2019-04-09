import os
import sys
import json
import psutil
import requests

log_file_path = "/var/log/apt/history.log"
__path__ = f"{os.getcwd()}/src/"
__CONFIG__ = json.load(open(f"{__path__}configs.json","r"))

def get_hardware_use():
    """
    Shows python's hardware consumption and total memory/cpu usage
    """
    gb = 1_024_000_000.0
    pid = os.getpid()
    python_cpu_usage = psutil.Process(pid).cpu_percent()
    cpu_usage_in_percentage = psutil.cpu_percent()
    total_memory_in_gb = psutil.virtual_memory().total/gb
    used_memory_in_gb = psutil.virtual_memory().used/gb
    available_memory_in_gb = total_memory_in_gb - used_memory_in_gb

    info = f""" 
                python cpu usage: {python_cpu_usage} %
                cpu usage: {cpu_usage_in_percentage} %
                used memory: {used_memory_in_gb} GB
                available memory: {available_memory_in_gb} GB
            """
    return info


def json_apt_history_info():
    """
    Generates a json file with apt history. It is saved as json_log.json
    """
    with open(log_file_path, "r") as log_file:
        content = {"history":[]}
        data = {}

        for line in log_file.readlines():
            if line is "\n":
                content["history"].append(data) 
                data = {}
                continue
            
            key, value = line.split(": ")
            data[key] = value[:-1]
            
        
        with open(f"{__path__}json_log.json", "w") as jsonlog:
            content["history"] = content["history"][1:]
            jsonlog.write(json.dumps(content))
            
            
                

def get_weather_from_city(city, country):
    """
    gets weather from the given city of a specific country
    and saves on a file called 'weather_content.txt'
    """
    with open(f"{__path__}weather_content.json","w") as f:
        key = __CONFIG__["weather_api_key"]
        base_url = __CONFIG__["base_url"]
        url = f"{base_url}/data/2.5/weather?q={city},{country}&APPID={key}"
        res = requests.get(url)
        f.write(res.text)


if __name__ == "__main__":
    try:
        get_weather_from_city(sys.argv[1], sys.argv[2])
        json_apt_history_info()
        print(get_hardware_use())
    except :
        print("Error - usage: python scripting.py 'city name' 'country name (2 letters code)'")
