cmake_minimum_required (VERSION 3.5.1)

project (Examples NONE)

find_program (MAKE make)
message(${MAKE})

find_program (MYPY mypy)
message(${MYPY})

find_program (PYLINT pylint)
message(${PYLINT})

find_program (PYTHON python3)
message(${PYTHON})

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

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)

add_custom_target (run)

add_custom_target (CommandLine.pyx
    COMMAND echo -${MYPY}   ../CommandLine.py
    COMMAND      -${MYPY}   ../CommandLine.py
    COMMAND echo -${PYLINT} ../CommandLine.py
    COMMAND      -${PYLINT} ../CommandLine.py
    COMMAND echo ${PYTHON}  ../CommandLine.py nothing to be done
    COMMAND      ${PYTHON}  ../CommandLine.py nothing to be done
    DEPENDS .pylintrc)
add_custom_command (TARGET run
    COMMAND ${MAKE} CommandLine.pyx)

foreach (file ${FILES})
    add_custom_target (${file}.pyx
        COMMAND echo -${MYPY}   ../${file}.py
        COMMAND      -${MYPY}   ../${file}.py
        COMMAND echo -${PYLINT} ../${file}.py
        COMMAND      -${PYLINT} ../${file}.py
        COMMAND echo ${PYTHON}  ../${file}.py
        COMMAND      ${PYTHON}  ../${file}.py
        DEPENDS .pylintrc)
    add_custom_command (TARGET run
        COMMAND ${MAKE} ${file}.pyx)
endforeach ()

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES ".mypy_cache")
