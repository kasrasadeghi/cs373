# -----------
# Fri, 30 Jun
# -----------

# singleton design pattern

# Java
class A {
    public final static A only = A()

    private A () {}

    void f () {...}}

class T {
    public void static main (...) {
        A x = new A(); # not ok
        A x = A.only;
        x.f();
        A.only.f();

# old A
x = A() # invoke A's constructor
        # make an instance of A

# new A
y = A() # invoking a lambda
        # which returns an instance of A

# finish Decoration
# couple of misc things
# class in Python

x = range_iterator(2, 4)
p = iter(x)
print(x is p) # true

print(list(x)) # [2, 3]
print(list(x)) # []

x = range_iterable(2, 4)
p = iter(x)
print(x is p) # false

print(list(x)) # [2, 3]
print(list(x)) # [2, 3]

def make_iterable (c) :
    class foo :
        def __init__ (self, *b, **e) :
            self.b = b
            self.e = e

        def __iter__ (self) :
            return c(*self.b, **self.e)

    return foo

x += y        """is that the same as?"""      x = x + y
