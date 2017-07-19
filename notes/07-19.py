# -----------
# Wed, 19 Jul
# -----------

class A {
    public void void f (int i) {g(i);}
    public static void g (int) {...}

class B extends A {
    public static void g (int) {...}}

class T {
    public static void main (...) {
        A x = new B();
        x.f(2);        // A.g

# reflection in Java

class A {
    ...}

class B  {
    ...}

class T {
    public static void main (...) {
        Class c = A.class;
        A x = new A();
        Class c2 = x.getClass();
        assert(A.class == x.getClass());
        assert(c == c2);

        Class c3 = Class.forName("B");   # static method
        A     y  = (A) c3.newInstance(); # non-static method

"""
forName will fail
    with an invalid name
newInstance will fail
    no default constructor
    abstract class
    interface
    potentially a non-public constructor
cast will fail
    not done correctly
"""

class A {}

class T {
    public static void main (...) {
        A x = new A();


# ---------
# Questions
# ---------

"""
In Java what is class Class?
What is forName()?
What is newInstance()?
What are all the error cases for both?
In Python what is type type?
What is globals()?
What are its error cases?
"""
