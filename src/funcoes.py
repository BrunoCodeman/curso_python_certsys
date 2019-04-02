#dir, help, void, defs, try-catch, lambdas,open, map, filter, args, kwargs, dict no lugar de if/else
import json

melhor_alemao = '{"nome":"Karl Marx", "profissão": "Advogado"}'
dict_melhor_alemao = json.loads(melhor_alemao)
print(dict_melhor_alemao)

def filter_divisible_by_two(arr: list) -> list:
    """Filters all elements in a list that are divisible by two"""
    pass

def multiply_array_by_ten(arr: list) -> list:
    """Multiplies all elements in a list by ten"""
    pass

def replace_values_in_a_dict_by_a_new_one(d: dict, new_value: object) -> dict:
    """Replaces all the values in a dictionary by a given value"""
    pass

def add_line_to_file(file_path: str, line: str):
    """Adds a new line to a given file"""
    pass

def make_full_name(name: str, lastname: str)-> str:
    """Makes a string with a full name"""
    pass

def read_config_as_dict_from_json_file(file_path)-> dict:
    """Reads a configuration file to a dictionary object"""
    pass

def dict_values_separated_by_given_char(d:dict , char: chr) -> str:
    """
    Creates a string with all the values of a dictionary separated by a given character
    """
    pass


