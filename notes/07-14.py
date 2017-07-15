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

# ---------
# Questions
# ---------

"""
What are the multiplicities of Customer, Rental, and Movie in Fowler's example?
The refactoring that everyone thought of in yesterday's exercise is called "Replace Type Code with Subclasses". What was the downside of that refactoring for that problem?
The refactoring that Fowlder did is called "Replace Type Code with State / Strategy". How is that different?
Did that refactoring completely remove the switch statement or just move it?
If only moved, what's the benefit of the refactoring?
"""
