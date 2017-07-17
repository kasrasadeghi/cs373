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
    private void f () {...}
    public void g () {f();}

class B extends A {
    private void f ()  {...}

class T {
    public static void main (...) {
        A y = new B();
        y.g();         // A.f

"""
Java can inline methods:
    1. final method
    2. final class
    3. static method
    4. private method
"""

class A {
    private static A _only;

    private A () {}

    public static A only () {
        if (_only == null)
            _only = new A();
        return _only;}}

class A {
    private static A _only = new A();

    private A () {}

    public static A only () {
        return _only;}}

# ---------
# Questions
# ---------

"""
What is an abstract class? Abstract method?
What is a final class? Final method?
What is an inline method?
When are methods not dynamically bound and therefore eligible to be inlined?
What's better about an abstract method compared to a non-abstract method?
What's an eager singleton? A lazy singleton?
"""
