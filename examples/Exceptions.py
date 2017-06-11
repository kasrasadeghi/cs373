#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3.5/tutorial/errors.html#exceptions

def f (b) :
    if b :
        raise NameError("abc")
    return 0

print("Exceptions.py")

try :
    assert f(False) == 0
except NameError :
    assert False
else :                   # no exception vs. raised and handled
    pass                 # but not with break, continue, return
finally :                # always
    pass                 # even with break, continue, return

try :
    assert f(True) == 1
    assert False
except NameError as e :
    assert isinstance(e,      NameError)
    assert isinstance(e.args, tuple)
    assert len(e.args)  ==     1
    assert e.args       is not ("abc",)
    assert e.args       ==     ("abc",)
else :                                   # no exception vs. raised and handled
    assert False                         # but not with break, continue, return
finally :                                # always
    pass                                 # even with break, continue, return

assert isinstance(NameError,     type)
assert isinstance(NameError,     object)

assert isinstance(type,          type)
assert isinstance(type,          object)

assert isinstance(object,        object)

assert issubclass(NameError,     NameError)
assert issubclass(NameError,     Exception)
assert issubclass(NameError,     BaseException)
assert issubclass(NameError,     object)

assert issubclass(Exception,     Exception)
assert issubclass(Exception,     BaseException)
assert issubclass(Exception,     object)

assert issubclass(BaseException, BaseException)
assert issubclass(BaseException, object)

assert issubclass(type,          type)
assert issubclass(type,          object)

assert issubclass(object,        object)

print("Done.")
