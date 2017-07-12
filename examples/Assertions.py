#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

def cycle_length_1 (n: int) -> int :
    assert n > 0
    if n == 1 :
        c = 1
    elif (n % 2) == 0 :
        c = 1 + cycle_length_1(n // 2)
    else :
        c = 1 + cycle_length_1((3 * n) + 1)
    assert c > 0
    return c

def cycle_length_2 (n: int) -> int :
    def f (m: int, n: int) :
        assert n > 0
        if n == 1 :
            c = m
        elif (n % 2) == 0 :
            c = f(m + 1, n // 2)
        else :
            c = f(m + 1, (3 * n) + 1)
        assert c > 0
        return c
    return f(1, n)

def cycle_length_3 (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

print("Assertions.py")

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

assert cycle_length_2( 1) == 1
assert cycle_length_2( 5) == 6
assert cycle_length_2(10) == 7

assert cycle_length_3( 1) == 1
assert cycle_length_3( 5) == 6
assert cycle_length_3(10) == 7

print("Done.")

""" #pragma: no cover
% Assertions.py
Assertions.py
Traceback (most recent call last):
  File "Assertions.py", line 55, in <module>
    assert cycle_length_2( 1) == 1
  File "Assertions.py", line 34, in cycle_length_2
    assert c > 0
AssertionError



% python3 -O Assertions.py
Assertions.py
Done.
"""
