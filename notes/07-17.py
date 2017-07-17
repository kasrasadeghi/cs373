# -----------
# Mon, 17 Jul
# -----------

"""
a few more refactorings
"""

"""
what are the consequences of an abstract method

1. the class must be declared abstract
2. the children must either implement or become abstract
3. the method in the base class is either
    a. required
    b. not allowed (Java)
    c. optional (C++)
"""

# Java
class A {
    public void f (int) {...}
    public abstract void g (long) {...}
    public final void h (int) {...}

class B extends A {
    public void f (int) {...}
    public void g (int) {...}

class A {
    public void f (int)  {...}
    public void g (int)  {...}
    public void h (long) {...}

class B extends A {
    public void f (int)  {...}
    public void g (long) {...}
    public void h (int)  {...}

class T {
    public static void main (...) {
        B x = new B();
        x.f(2);        // B.f
        x.g(2);        // A.g
        x.h(2);        // B.h

        A y = new B();
        y.f(2);        // B.f
        y.g(2);        // A.g
        y.h(2);        // A.h

class A {
    public void f (int)  {...}

class B extends A {
    public void f (int)  {...}

class T {
    public static void main (...) {
        A y;
        if (...)
            y = new A();
        else
            y = new B();
        y.f(2);




















