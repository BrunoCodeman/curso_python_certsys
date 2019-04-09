import os
import getpass
import json
import unittest
from src import scripting 

class ScriptingTest(unittest.TestCase):

    def setUp(self):
        self.path = f"{os.getcwd()}/src/"
        return super().setUp()

    def test_must_generate_weather_file(self):
        name = "Sao Paulo"
        country = "BR"
        scripting.get_weather_from_city(name, country)
        cod = 200
        _id = 3448439       
        conditions = ["country","id","name","cod"]
        
        
        with open(f"{self.path}weather_content.json") as file_content:
            content = json.loads(file_content.read())
            self.assertEqual(content["id"], _id)
            self.assertEqual(content["name"], name)
            self.assertEqual(content["cod"], cod)
            self.assertEqual(content["sys"]["country"], country)


    def test_must_generate_apt_file(self):
        
        key = "Requested-By"
        user = getpass.getuser()
        first = lambda x: key in x.keys() and user in x[key]
        second = lambda y: y[key]
        scripting.json_apt_history_info()
        with open(f"{self.path}json_log.json") as jsonlogfile:
            file_content = jsonlogfile.read()
            log_content = json.loads(file_content)
            requested_by = list(map(second,filter(first, log_content["history"])))
            self.assertNotEqual(len(requested_by),0)
                

    def test_must_get_memory_and_cpu_usage(self):
        expected = ["python cpu usage:","cpu usage:",
                    "used memory:","available memory:"]
        actual = scripting.get_hardware_use() 
        for e in expected:
            self.assertTrue(e in actual)
        