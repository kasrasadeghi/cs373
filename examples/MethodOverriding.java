// ---------------------
// MethodOverriding.java
// ---------------------

class A {
    public String f (int i) {
        return "A.f";}

    public String g (int i) {
        return "A.g";}

    public String h (long l) {
        return "A.h";}}

class B extends A {
    public String f (int i) {
        return "B.f";}

    public String g (long l) {
        return "B.g";}

    public String h (int i) {
        return "B.h";}}

final class MethodOverriding {
    public static void main (String[] args) {
        System.out.println("MethodOverriding.java");

        B x = new B();

        assert x.f(2)  == "B.f";
        assert x.g(2)  == "A.g";
        assert x.g(2L) == "B.g";
        assert x.h(2)  == "B.h";
        assert x.h(2L) == "A.h";

        A y = new B();

        assert y.f(2)  == "B.f";
        assert y.g(2)  == "A.g";
//      assert y.g(2L) == "A.g"; // error: incompatible types: possible lossy conversion from long to int
        assert y.h(2)  == "A.h";
        assert y.h(2L) == "A.h";

        System.out.println("Done.");}}
