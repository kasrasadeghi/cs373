# -----------
# Wed, 14 Jun
# -----------

"""
semantics of the operator and types in Python
start exploring in detail iteration and iterables in Python
"""

def f (n: int) -> int :
    if (n <= 1)
        return 1
    return n * f(n - 1)

def f (n: int) -> int :
    m = 1
    while (n > 0) :
        m *= n
        n -= 1
    return m

a = [2, 3, 4]
p = iter(a)
print(next(p)) # 2
print(next(p)) # 3
print(next(p)) # 4
print(next(p)) # raise StopIteration

# ---------
# Questions
# ---------

"""
What is a recursive procedure? Recursive process?
What is tail recursion?
Why don't containers allow direct iteration?
What is iter()?
What do iterators do when they're exhausted?
What is range() and xrange() in Python 2?
What is range() in Python3?
What is reduce()?
"""
