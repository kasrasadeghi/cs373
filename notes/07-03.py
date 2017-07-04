# -----------
# Mon,  3 Jul
# -----------

"""
Java has 4 access directives
    public
    protected: descendents and package
    private
    nothing: package

class A {
    private static int _ci;
    private        int _i;

    public A (...) {
        ...}}

class T {
    public static void main (...) {
        s.o.p(A._i); // not ok
        s.o.p(A._ci);
        x = new A(...);
        s.o.p(x._i);
        s.o.p(x._ci); // yes, but odd

Java has a closed object model
    instances have the same footprint over time
    different instances have the same footpring

Python has an open object model
    instances don't have the same footprint over time
    different instances don't have the same footpring
"""

class A :
    def __init__ (self) :
        self.velocity = 2

x = A()
print(x.velocity) # 2
x.velocityy = 3

a = [A(...), A(...), A(...)]
m = map(A.im, a)

"""
relational algebra is an algebra

algebra
    set of elements
    set of operations

integer
    -3, 2, 5, 0, ...
    +, -, /, *, ...

are algebras closed or open

integers over addition:       closed
integers over multiplication: closed
integers over division:       open

relational algebra
    relations, tuples, tables with rows
    select, project, join (several kinds)

movie table
title year director genre
shane 1953 george stevens western
star wars 1977 george lucas western

select
    relation
    unary predicate (unary function that returns a bool)
"""

select (movie, lambda r : year > 1970)

x = [["shane", 1953, "george stevens", "western"]
     ["star wars", 1977, "george lucas", "western"]]

def select (iterable, callable) :
    for i in iterable :
        if callable(i) :
            yield i

def select (iterable, callable) :
    return (i for i in iterable if callable(i))

def select (iterable, callable) :
    return filter(callable, iterable)

# ---------
# Questions
# ---------

"""
What is a closed/open object model? Which language has which?
What is a closed/open algebra?
What data structure in Python can mimic a relation?
What is select()?
What is project()?
"""
