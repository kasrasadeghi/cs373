cmake_minimum_required (VERSION 3.8.2)

project (Quizzes NONE)

set (FILES
    Hello
    Exceptions
    Types
    Operators
    Variables
    Iteration
    Comprehensions
    Yield
    Iterables
    FunctionKeywords
    FunctionDefaults
    FunctionUnpacking
    FunctionTuple
    FunctionDict
    Functions
    Copy
    Cache
    MyPy
    Classes)

enable_testing()

foreach (file ${FILES})
    add_test (${file} ../${file}.py)
endforeach ()
