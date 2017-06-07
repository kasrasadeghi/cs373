# ----------
# Wed, 7 Jun
# ----------

"""
(3n + 1) / 2
3n/2 + 1/2
3n/2 + 1
n + n/2 + 1
n + (n >> 1) + 1

explore the nature of testing

assertions
    for preconditions, postconditions, loop invariants
    for programmer errors

    not good for user errors, a good solution will exceptions
    not good for unit tests, a good solution is a unit test framework

Python has a module called unittest

"""

# Java
class A {
    public void f () {
        g();
        this.g();}

    public void g () {...}}

class T {
    public static void main (...) {
        A x = new A;
        x.f();

        A y = new A;
        y.f();

# Python

def g (...) :
    ...

class A :
    def f (self) :
        self.g()

    def g (self) :
        ...

"""
exercise to demonstrate that bad tests can hide bad code

1. identify the broken tests
2. fix the tests
3. now the code fails
4. fix the code
"""

#h = 0

def f (..., e2) :
#    global h
    ...
    if (...)
        # something is wrong
        e2[0] = -1
        return ...
    ...

def g (...) :
#    global h
    ...
#    h = 0
    e = [0]
    x = f(..., e)
    if (e[0] == -1)
        # something wrong

...
g(...)
...

# ---------
# Questions
# ---------

"""
Explain the n + (n >> 1) + 1 optimization.
What are assertions good for? Not good for?
What's a good solution for unit testing?
What is unittest::main?
What is unittest:TestCase?
What is if __name__ == "__main__" ?
What is #pragma: no cover?
Will an internal assertion failure stop unittest?
What is coverage?
What values does range(n)    produce?
What values does range(m, n) produce?
Other than exceptions, what are the three avenues of communication?
"""
