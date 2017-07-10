#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

def cycle_length_recursion (n: int) -> int :
    assert n > 0
    if n == 1 :
        c = 1
    elif (n % 2) == 0 :
        c = 1 + cycle_length_recursion(n // 2)
    else :
        c = 1 + cycle_length_recursion((3 * n) + 1)
    assert c > 0
    return c

def cycle_length_tail_recursion (n: int) -> int :
    assert n > 0
    def f (n: int, m: int) :
        if n == 1 :
            return m
        if (n % 2) == 0 :
            return f(n // 2, m + 1)
        return f((3 * n) + 1, m + 1)
    c = f(n, 1)
    assert c > 0
    return c

def cycle_length_iteration (n: int) -> int :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

print("Assertions.py")

assert cycle_length_recursion( 1) == 1
assert cycle_length_recursion( 5) == 6
assert cycle_length_recursion(10) == 7

assert cycle_length_tail_recursion( 1) == 1
assert cycle_length_tail_recursion( 5) == 6
assert cycle_length_tail_recursion(10) == 7

assert cycle_length_iteration( 1) == 1
assert cycle_length_iteration( 5) == 6
assert cycle_length_iteration(10) == 7

print("Done.")

""" #pragma: no cover
% Assertions.py
Assertions.py
Traceback (most recent call last):
  File "Assertions.py", line 59, in <module>
    assert cycle_length_iteration( 1) == 1
  File "Assertions.py", line 46, in cycle_length_iteration
    assert c > 0
AssertionError



% python3 -O Assertions.py
Assertions.py
Done.
"""
