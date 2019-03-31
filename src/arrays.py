#index, enumerate, append, del, slice, reverse, comprehension, copy


def slice_array_with_stepped_indexes(arr: list, index: int):
    """
    Slices an array with a given step
    
    Example: 
        slice_array_with_stepped_indexes([0,1,2,3,4,5,6], 2) returns [0,2,4,6]
    
    Args: 
    - arr: any ordinary list
    - index: the step wanted
    
    Returns:
    - A new array with only the elements on the stepped indexes
    """
    return arr[::index]

def reverse_array(arr: list):
    """
    Reverses a given array
    
    Args:
    - arr: any ordinary list
    
    Returns:
    - The given array reversed
    """
    return arr[::-1]

def remove_last_element_from_array(arr: list):
    """
    Removes the last element from an array
    
    Args:      
    - arr: any ordinary list
    
    Returns:
    - the same array given, but without the last element
    """
    return arr[:-1]

def add_next_number_to_array_of_integers(arr:list):
    """
    Adds a new number to a sequence of integers. 
    This number is is the next valid integer of the last number in array
    
    i.e: add_next_number_to_array([1,2,3]) returns [1,2,3,4]
    
    Args:      
    - arr: any ordinary list
    
    Returns:
    - An array of integers with a number added
    """
    arr.append(arr[-1]+1)
    return arr

def filter_odd_numbers(arr: list):
    """
    Filters all the odd numbers in a given array
    
    i.e: filter_odd_numbers([1,2,3,4,5]) returns [1,3,5]
    
    Args:      
    - arr: any ordinary list
    
    Returns:
    - an array only with odd numbers
    """
    return [e for e in arr if e % 2 == 1]

def multiply_all_elements_in_array_by_given_number(arr: list, n: int):
    """
    Multiply all the elements in a given array by a given value
   
    i.e: multiply_all_elements_in_array_by_given_number([1,2,3], 2) returns [2,4,6]
   
    Args:      
    - arr: any ordinary list
    - n: a number to multiply the array elements
   
    Returns:
    - an array with the elements multiplied by n
    """
    return [e*n for e in arr]

def get_all_indexes_from_array(arr: list, el: object):
    """
    Finds all the indexes of a given element in an array
   
    i.e get_all_indexes_from_array("banana","a") returns [1,3,5]
   
    Args:      
    - arr: any ordinary list
    - el: the object to search
   
    Returns:
    - a list with all the indexes where the element was found
    """
    return [i for i,e in enumerate(arr) if e is el]

def copy_array(arr: list):
    """
    Copies a given array
    
    Args:      
    - arr: any ordinary list
    
    Returns:
    - An exact copy of the given array
    """
    return arr[::]



if __name__ == "__main__":

    nome = "Bruno"
    lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
    idade = 33

    for i in lista:
        print(i)

    init = lista[0]

    print(lista)
    print(lista + list(nome))

    while(init in lista):
        
        print(f"init is {init}")
        
        if i % 2 == 0:
            print("init é par")
        else:
            print("init é impar")
        
        init+=1
    else:
        print("fim da lista")
