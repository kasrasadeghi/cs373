#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Functions.py
# ------------

print("Functions.py")

def square1 (v) :
    return v ** 2

class square2 :
    def __call__ (self, v) :
        return v ** 2

class square3 :
    def __init__ (self, w) :
        self.w = w

    def __call__ (self, v) :
        return v ** self.w

a = [2, 3, 4]
m = map(square1, a)
assert list(m) == [4, 9, 16]
assert list(m) == []

a = [2, 3, 4]
m = map(lambda v : v ** 2, a)
assert list(m) == [4, 9, 16]
assert list(m) == []

a = [2, 3, 4]
w = 2
m = map(lambda v : v ** w, a)
assert list(m) == [4, 9, 16]
assert list(m) == []

a = [2, 3, 4]
m = map(square2(), a)
assert list(m) == [4, 9, 16]
assert list(m) == []

a = [2, 3, 4]
w = 2
m = map(square3(w), a)
assert list(m) == [4, 9, 16]
assert list(m) == []

print("Done.")
