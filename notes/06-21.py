# -----------
# Wed, 21 Jun
# -----------

"""
finish the iteration story
comprehensions
generators
yield
"""

def f (v) :
    ...
    return v * 5

x = [2, 3, 4]
list(map(f, x)) # [10, 15, 20]
list(map(f, x)) # [10, 15, 20]

print(type(f)) # function

f = 2
print(f) # 2
print(type(f())) # int

f = lambda v : v * 5
x = [2, 3, 4]
list(map(f, x)) # [10, 15, 20]
list(map(f, x)) # [10, 15, 20]

d = {}
d[2] = "abc"
print(d) # {2: "abc"}

a = [2, 3, 4]
m = map(lambda v : v ** 2, a)
p = iter(m)    # m.__iter__()
print(m is p)  # True
print(next(m)) # 4, m.__next__()
print(next(m)) # 9
print(next(m)) # 16
print(next(m)) # raise StopIteration

class map :
    def __init__ (self, op, it) :
        self.op = op
        self.p  = iter(it)

    def __iter__ (self) :
        return self

    def __next__ (self) :
        return self.op(next(self.p))

class map :
    def __init__ (self, op, it) :
        self.gen = (op(x) for x in it)

    def __iter__ (self) :
        return self

    def __next__ (self) :
        return next(self.gen)

def f () :
    print("abc")
    yield 2
    print("def")
    yield 3
    print("ghi")

p = f() # <nothing>, magic
q = iter(p)
print(p is q) # True

v = next(p) # abc
print(v)    # 2

v = next(p) # def
print(v)    # 3

v = next(p) # ghi, raise StopIteration

def map (f, a) :
    for v in a :
        yield f(v)

def map (f, a) :
    return (f(v) for v in a)

# ---------
# Questions
# ---------

"""
What is a list comprehension?
What is a set  comprehension?
What is a dict comprehension?
What is a generator?
How do you create an empty set?
How do you distinguish a set comprehension from a dict comprehension?
Describe map().
Describe filter().
What is __init__()?
What is __iter__()?
What is __next__()?
How does iter() on a container differ from iter() on an iterator?
What is yield?
"""
