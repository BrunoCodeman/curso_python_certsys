import unittest
import datetime
from src.python_data_model import *


class PythonDataModelTest(unittest.TestCase):
    
    def test_multiply_list_must_be_iterable(self):
        size = 5
        multiplier = 4
        expecteds = [4,8,12,16,20]
        ml = MultiplyList(size, multiplier)
        _it = iter(ml)

        for i in expecteds:
            self.assertEqual(next(_it), i)
    
    def test_multiply_list_must_run_over_for_loop(self):
        size = 8
        multiplier = 10
        expecteds = [10, 20, 30, 40, 50, 60, 70, 80]
        ml = MultiplyList(size, multiplier)
        
        for i in ml:
            self.assertIn(i, expecteds)
        

    def test_person_class_must_have_age_property(self):
        birth_date, name = datetime.datetime(1985,12,14), "Bruno"
        _person = Person(birth_date, name)
        self.assertEqual(_person.age, 33)

    def test_account_must_be_callable(self):
        birth_date, name = datetime.datetime(1985,12,14), "Bruno"
        _person = Person(birth_date, name)
        _expected = f"{name} has {_person.age} years"
        self.assertEqual(_person(), _expected)
