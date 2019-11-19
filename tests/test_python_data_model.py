import unittest
from src.python_data_model import *


class PythonDataModelTest(unittest.TestCase):
    

    def test_multiply_list_must_be_iterable(self):
        multiplier = 4
        ml = MultiplyList(5, multiplier)
        _it = iter(ml)
        self.assertEqual(next(_it), 4)
        self.assertEqual(next(_it), 8)
        self.assertEqual(next(_it), 12)
        self.assertEqual(next(_it), 16)
        self.assertEqual(next(_it), 20)
    
    def test_multiply_list_must_run_over_for_loop(self):
        multiplier = 4
        ml = MultiplyList(5, multiplier)
        
        for i in ml:
            self.assertEqual(i, )
        

    def test_account_must_have_balance_property(self):
        pass

    def test_account_must_be_callable(self):
        pass