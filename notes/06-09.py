# ----------
# Fri, 9 Jun
# ----------

y[0] = -1

y[:] = ? # not ok

"""
2
10
15

lazy cache is remembering on input
eager cache would remember before inputting
meta cache would remember outside of the program

testing
    assertions -> unittest
    exceptions
"""

def f () :
    ...
    if (...)
        raise E(...)
    ...

def g () :
    ...
    try :
        ...
        x = f(...)
        ...
    except E as e :
        ...
        raise e
    except F as e :
        ...
    else :
        ...
    finally : # better name would be always
        ...
    ...

...
...g(...)...
...

"""
1. no exception was raised in f(), this is when else runs
2. exception was raised that g() handles
3. exception was raised that g() doesn't handle
"""

x = [2, 3, 4]
print(type(x)) # list, lists are mutable

x = (2, 3, 4)
print(type(x)) # tuple, tuples are no mutable

# Java
Integer z = new Integer();
Integer x = new Integer(2);
Integer y = new Integer(2);
System.out.print(x == y);      // false, identity equality
System.out.print(x.equals(y)); // true,  object   equality

# Python
x = [2, 3, 4]
y = [2, 3, 4]
print(x == y) # true,  object   equality
print(x is y) # false, identity equality

x = [2, 3]
print(type(x)) # list
x = [2]
print(type(x)) # list

x = (2, 3)
print(type(x)) # tuple
x = (2)
print(type(x)) # int
x = (2,)
print(type(x)) # tuple

print(type(2))    # int
print(type(int))  # type
print(type(type)) # type

"""
elements of list/tuple can be anything

Java
TreeSet: red-black binary tree, elements have to be comparable
HashSet: hashtable, elements have to be hashable

TreeMap
HashMap

Python
of the types in the language, only the immutables are hashable

the immutables
    int
    float
    string
    tuple
    frozenset

the mutables
    list
    set
    dict
"""

# ---------
# Questions
# ---------

"""
What is a lazy cache? Eager cache? Meta cache?
What is the except clause? Else clause? Finally clause?
What is rethrowing?
What is type? object?
What type of elements can be in a list? Tuple? String?
What type of elements can be in a set? Dict?
What are the immutables? Mutables?
"""
