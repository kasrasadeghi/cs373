cmake_minimum_required (VERSION 3.8.2)

project (Examples NONE)

find_program(MYPY   mypy)
find_program(PYLINT pylint)

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

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)

add_custom_target (.pylintrcx ALL DEPENDS .pylintrc)

enable_testing()

foreach (file ${FILES})
    add_test (${file}.mypy   ${MYPY}   ../${file}.py)
    add_test (${file}.pylint ${PYLINT} ../${file}.py)
    add_test (${file}                  ../${file}.py)
endforeach ()

add_custom_target (versions)

set (PRGS
    cmake
    make
    mypy
    pylint)

foreach (prg ${PRGS})
    add_custom_command (TARGET versions
        COMMAND echo which ${prg}
        COMMAND      which ${prg}
        COMMAND echo ${prg} --version
        COMMAND      ${prg} --version
        COMMAND echo)
endforeach ()
