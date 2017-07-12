cmake_minimum_required (VERSION 3.8.2)

project (Examples NONE)

find_program (MAKE make)
message(${MAKE})

find_program (MYPY mypy)
message(${MYPY})

find_program (PYLINT pylint)
message(${PYLINT})

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
    Classes
    RegExps
    Test)

enable_testing ()

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)
add_custom_target  (.pylintrcx DEPENDS .pylintrc)
add_test           (.pylintrc  ${MAKE} .pylintrcx)

foreach (file ${FILES})
    add_test (${file}.mypy   ${MYPY}   ../${file}.py)
    add_test (${file}.pylint ${PYLINT} ../${file}.py)
    add_test (${file}                  ../${file}.py)
endforeach ()

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES ".coverage" ".mypy_cache")
