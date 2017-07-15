# -----------
# Fri, 14 Jul
# -----------

class A {
    void f () {...}}

class B extends A {
    void f () {...}};

class T {
    public static void main (...) {
        A x;
        if (...)
            x = new A();
        else
            x = new B();
        x.f();
