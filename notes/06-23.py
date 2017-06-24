# -----------
# Fri, 23 Jun
# -----------

p = f
print(p is f) # True

x = range(2, 5)
print(type(x)) # range
v = next(x)    # not ok
p = iter(x)
print(x is p)  # False
print(type(p)) # range iterator
q = iter(p)
print(p is q)  # True
v = next(p)
print(v)       # 2
v = next(p)
print(v)       # 3
v = next(p)
print(v)       # 4
v = next(p)    # raise StopIteration

class range_iterator :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return self

    def __next__ (self) :
        if self.b == self.e :
            raise StopIteration
        b = self.b
        self.b += 1
        return b

def range_iterator (b, e) :
    while b != e :
        yield b
        b += 1

"""
three tokens: =, *, **
two contexts: function call, function definition
"""

# ---------
# Questions
# ---------

"""
Is range a container or a an iterator?
What's the danger in using a mutable as a default value?
Describe * in a function call.
Describe * in a function definition (two cases).
Describe ** in a function call.
Describe ** in a function definition.
Describe = in a function call.
Describe = in a function definition.
"""
