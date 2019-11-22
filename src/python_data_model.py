import datetime

class MultiplyList:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0, mult=1):
        self.max = max
        self.mult = mult
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.mult * self.n
            self.n += 1
            return result
        else:
            raise StopIteration
    def __delitem__(self, key):
        self.__delattr__(key)
    def __getitem__(self, key):
        return self.__getattribute__(key)
    def __setitem__(self, key, value):
        self.__setattr__(key, value)




class Person:

    def __init__(self, birth_date, name):
        self.birth_date = birth_date
        self.name = name

    @property
    def age(self):
        _date = datetime.datetime.now() - self.birth_date
        return int(_date.days/365)

    def __call__(self):
        return f"{self.name} has {self.age} years"
