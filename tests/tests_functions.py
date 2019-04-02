import os
import unittest
from src import funcoes

class FunctionsTest(unittest.TestCase):

    def test_must_filter_divisible_by_two(self):
        arr = [0,1,2,3,4,5,6,7,8,9]
        expected = [0,2,4,6,8]
        actual = funcoes.filter_divisible_by_two(arr)
        self.assertEqual(type(actual), filter)
        self.assertEqual(list(actual), expected)
        

    def test_must_multiply_array_by_ten(self):
        arr = [1,2,3,4,5]
        expected = [10, 20, 30, 40, 50]
        actual = funcoes.multiply_array_by_ten(arr)
        self.assertEqual(type(actual), map)
        self.assertEqual(list(actual), expected)

    def test_must_replace_values_in_a_dict_by_a_new_one(self):
        value = "Socialização dos meios de produção"
        arr = {
                "solucao_brasil": "Menos estado", 
                "solucao_eua": "Presidente laranja"
            }
        expected = {
                "solucao_brasil": value, 
                "solucao_eua": value
            }
        actual = funcoes.replace_values_in_a_dict_by_a_new_one(arr, value)
        self.assertEqual(actual, expected)

    def test_must_add_line_to_file(self):
        content = ""
        line = "\nAo rico tudo é permitido"
        file_path = f"{os.getcwd()}/src/a_internacional.txt"
        funcoes.add_line_to_file(file_path, line)
        with open(file_path, "r") as f:
            content = f.read()
        self.assertTrue(line in content)

    def test_must_read_config_as_dict_from_json_file(self):
        file_path = f"{os.getcwd()}/src/configs.example.json"
        key, value = "password", "cump3t4"
        res = funcoes.read_config_as_dict_from_json_file(file_path)
        self.assertTrue(key in res.keys())
        self.assertTrue(value in res.values())

    def test_must_return_dict_values_separated_by_given_char(self):
        d = { 
                "solucao_campesina": "coletivização de latifúndios",
                "solucao_industrial": "tomadas dos meios privados de produção"
            }
        separador = ","
        expected = "coletivização de latifúndios,tomadas dos meios privados de produção"
        actual = funcoes.dict_values_separated_by_given_char(d, separador)
        self.assertEqual(actual, expected)
    

    def test_must_return_name_and_lastname(self):
        full_name = ["Friedrich", "Engels"]
        expected = "Friedrich Engels"
        actual = funcoes.make_full_name(*full_name)
        self.assertEqual(actual, expected)
        
    

