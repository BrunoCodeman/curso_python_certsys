import unittest
from src import arrays

class ArrayTest(unittest.TestCase):


    def test_array_must_jump_two(self):
        step = 2
        arr = [0,1,2,3,4,5,6,7,8,9,10]
        expected = [0, 2, 4, 6, 8, 10]        
        actual = arrays.slice_array_with_stepped_indexes(arr, step)
        self.assertEqual(expected, actual)

    def test_must_return_a_reversed_string(self):
        value = "certsys"
        expected = "systrec"
        actual = arrays.reverse_array(value)
        self.assertEqual(expected, actual)

    def test_array_without_last_element(self):
        value = [0,1,2,3,4,5,6,7,8,9,10]
        expected = [0,1,2,3,4,5,6,7,8,9]      
        actual = arrays.remove_last_element_from_array(value)
        self.assertEqual(expected, actual)

    def test_add_number_to_array(self):
        value = [0,1,2,3,4,5,6,7,8,9]      
        expected = [0,1,2,3,4,5,6,7,8,9,10]
        actual = arrays.add_next_number_to_array_of_integers(value)
        self.assertEqual(expected, actual)

    def test_filter_odd_numbers(self):
        value = [0,1,2,3,4,5,6,7,8,9,10]
        expected = [1,3,5,7,9]        
        actual = arrays.filter_odd_numbers(value)
        self.assertEqual(expected, actual)
    
    def test_multiply_all_numbers_in_array_by_two(self):
        n = 2
        value = [1,2,3,4,5]
        expected = [2, 4, 6, 8, 10]        
        actual = arrays.multiply_all_elements_in_array_by_given_number(value, 2)
        self.assertEqual(expected, actual)
    
    def test_multiply_all_elements_in_array_by_two(self):
        n = 2
        value = ["a","b","c"]
        expected = ["aa","bb","cc"]        
        actual = arrays.multiply_all_elements_in_array_by_given_number(value, 2)
        self.assertEqual(expected, actual)
    
    def test_get_all_indexes_from_array(self):
        el = "a"
        arr = "banana"
        expected = [1,3,5]        
        actual = arrays.get_all_indexes_from_array(arr, el)
        self.assertEqual(expected, actual)

    def test_copy_array(self):
        arr = [1,2,3]
        not_expected = id(arr)
        actual = id(arrays.copy_array(arr))
        self.assertNotEqual(actual, not_expected)
