
''' A generator is a kind of iterator that is defined with normal function
that contains a yield statement is called a generator.'''

nested = [[1, 2], [3, 4], [5]]

def flatten1(nested):
    for sublist in nested:
        for element in sublist:
            yield element


''' Each time a value is yielded (with yield), the function freezes;
that is, it stops its execution at exactly that point and waits to be reawakened.
When it is, it resumes its execution at the point where it stopped. '''

for num in flatten(nested):
    print(num)
    
'''
1
2
3
4
5

or

'''
list(flatten(nested))

'[1, 2, 3, 4, 5]'


# Loopy Generator:

g = ((i + 2) ** 2 for i in range(2, 27))
next(g)

'16'

# you can write pretty code like this:

sum(i ** 2 for i in range(10))


# if you have a set of lists nested arbitrarily deeply-

def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested

list(flatten2([[[1], 2], 3, 4, [5, [6, 7]], 8]))

'[1, 2, 3, 4, 5, 6, 7, 8]'


''' If nested is a string or string-like object,
it is a sequence and will not raise TypeError,
yet you do not want to iterate over it. '''


def flatten3(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield nested

list(flatten3(['foo', ['bar', ['baz']]]))

"['foo', 'bar', 'baz']"





