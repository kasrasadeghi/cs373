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














