#{}, dict(), dict() c/ lista de tuplas, update, comprehension, keys,values, items,

def get_keys_from_dict(d: dict):
    """
    Returns a list with the keys of a dict
    """
    return list(d.keys())

def get_values_from_dict(d: dict):
    """
    Returns a list with the values of a dict
    """
    return list(d.values())

def transform_two_lists_into_dict(key_list: list, value_list: list):
    """
    Transforms two lists in a single array of keys and values
    """
    return dict(zip(key_list, value_list))

def switch_keys_and_values(d: dict):
    """
    Switch the keys of a dictionary by its values
    """
    return {v:k for k,v in d.items()}

def merge_two_dicts(first_dict:dict , second_dict:dict ):
    """
    Creates a dict with the content of the given dicts
    """
    first_dict.update(second_dict)
    return first_dict

def remove_non_string_indexes(d: dict):
    """
    Removes all indexes from a dict that are not strings
    """
    new = {k:v for (k,v) in d.items() if type(k) is not int }
    return new

um_dicionario = dict(a=1, b=2, c=3)
outro_dicionario = { "a": 1, "b":2, "c":3 }
print(um_dicionario is outro_dicionario)
