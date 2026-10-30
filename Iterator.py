
'''More formally, an object that implements the __iter__ method is iterable, and the object
implementing __next__ is the iterator.'''

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self): # next(iterator) function -- returns next value or raise a StopIteration exception
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self): # iter(iterable_obj) function -- returns an iterator
        return self

fibs = Fibs()

# find the smallest Fibonacci number that is greater than 1,000
for f in fibs:
    if f > 1000:
        print(f)
        break

'''
The built-in function iter can be used to get an iterator from an iterable object.

>>> it = iter([1, 2, 3])
>>> next(it)
1
>>> next(it)
2


Making sequence from iterators

class TestIterator:
... value = 0
... def __next__(self):
... self.value += 1
... if self.value > 10: raise StopIteration
... return self.value
... def __iter__(self):
... return self
...
>>> ti = TestIterator()
>>> list(ti)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'''


















