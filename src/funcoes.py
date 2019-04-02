#dir, help, void, defs, try-catch, lambdas,open, map, filter, args, kwargs, dict no lugar de if/else
import json

melhor_alemao = '{"nome":"Karl Marx", "profissão": "Advogado"}'
dict_melhor_alemao = json.loads(melhor_alemao)

print(dict_melhor_alemao)

def filter_divisible_by_two(arr: list) -> list:
    """Filters all elements in a list that are divisible by two"""
    return filter(lambda x: x % 2 ==0, arr)

def multiply_array_by_ten(arr: list) -> list:
    """Multiplies all elements in a list by ten"""
    return map(lambda x: x * 10, arr)

def replace_values_in_a_dict_by_a_new_one(d: dict, new_value: object) -> dict:
    """Replaces all the values in a dictionary by a given value"""
    return {k:new_value for k in d.keys()}

def add_line_to_file(file_path: str, line: str):
    """Adds a new line to a given file"""
    with open(file_path,"a+") as f:
        f.write(line)


def make_full_name(name: str, lastname: str)-> str:
    """Makes a string with a full name"""
    return f"{name} {lastname}"

def read_config_as_dict_from_json_file(file_path)-> dict:
    """Reads a configuration file to a dictionary object"""
    with open(file_path,"r") as f:
        return json.load(f)

def dict_values_separated_by_given_char(d:dict , separator: str) -> str:
    """
    Creates a string with all the values of a dictionary separated by a given character
    """
    return separator.join(d.values())


def get_keys_and_values_from_dict(arr: dict):
    """
    Returns the keys and values of a dictionary splited in two lists
    """
    return arr.keys(), arr.values()