# -----------
# Mon, 19 Jun
# -----------

"""
further explore iteration
comprehensions
generators
yield
"""

def reduce (op, it, s) :
    p = iter(it)
    try :
        while (1) :
            s = op(s, next(p))
    except StopIteration :
        return s

def reduce (op, it, s) :
    for i in it :
        s = op(s, i)
    return s

"""
indexable (Sequence) vs iterable
algorithms need to be as undemanding as possible
container need to provide as strong a property as possible
"""

a = [2, 3, 4]
p = iter(a)
p = a.__iter__()
print(next(p))
print(p.__next__())

"""
list comprehensions are eager
generators are lazy

all generators are iterators
not all iterators are generators
"""

a = [2, 3, 4]
print(type(a)) # list
p = iter(a)
print(type(p)) # list iterator
print(a is p)  # false

q = iter(a)
print(type(q)) # list iterator
print(a is q)  # false
print(p is q)  # false

r = iter(p)
print(r is p)  # true

"""
iterable
    1. respond to iter()
    2. return an iterator from iter()

iterator
    1. respond to next()
    2. return items of the iterable from next()
    3. when exhausted raise StopIteration
    4. restpond to iter() with yourself!!!
"""

a = linked_list(...)
for v in a :
    f(v)

p = iter(a)
f1(next(p))
f2(next(p))
f3(next(p))

for v in p :
    f4(v)

"""
use tuples or other immutables with generators
"""

# ---------
# Questions
# ---------

"""
What is the definition of iterable? indexable?
Why can't you invoke next() directly on an iterable?
When can you use for-in with multiple looping variables?
What is the definition of iterator?
Why do iterators respond to iter() with themselves?
Give an example of something that is iterable, not indexable, and order doesn't matter.
Give an example of something that is iterable, not indexable, and order does matter.
What is a generator?
What does it mean to be lazy?
"""
