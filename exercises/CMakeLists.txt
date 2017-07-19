cmake_minimum_required (VERSION 3.5.1)

project (Exercises NONE)

message (${CMAKE_SOURCE_DIR})

find_program (COVERAGE coverage)
message      (${COVERAGE})

find_program (MAKE make)
message      (${MAKE})

find_program (MYPY mypy)
message      (${MYPY})

find_program (PYLINT pylint)
message      (${PYLINT})

find_program (PYTHON python3)
message      (${PYTHON})

set (FILES
    UnitTests3
    Coverage1
    Coverage2
    Coverage3
    IsPrime1
    IsPrime2
    Factorial
    Reduce
    Map
    RangeIterator
    Range
    Decorators
    Complex)

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)

add_custom_target (run)

add_custom_target (RMSET.pyx
    COMMAND echo -${PYLINT} ${CMAKE_SOURCE_DIR}/RMSE.py
    COMMAND      -${PYLINT} ${CMAKE_SOURCE_DIR}/RMSE.py
    COMMAND echo -${PYLINT} ${CMAKE_SOURCE_DIR}/RMSET.py
    COMMAND      -${PYLINT} ${CMAKE_SOURCE_DIR}/RMSET.py
    COMMAND echo ${PYTHON}  ${CMAKE_SOURCE_DIR}/RMSET.py
    COMMAND      ${PYTHON}  ${CMAKE_SOURCE_DIR}/RMSET.py
    DEPENDS .pylintrc)
add_custom_command (TARGET run
    COMMAND ${MAKE} RMSET.pyx)

foreach (file ${FILES})
    add_custom_target (${file}T.pyx
        COMMAND echo -${MYPY}                 ${CMAKE_SOURCE_DIR}/${file}.py
        COMMAND      -${MYPY}                 ${CMAKE_SOURCE_DIR}/${file}.py
        COMMAND echo -${PYLINT}               ${CMAKE_SOURCE_DIR}/${file}.py
        COMMAND      -${PYLINT}               ${CMAKE_SOURCE_DIR}/${file}.py
        COMMAND echo -${MYPY}                 ${CMAKE_SOURCE_DIR}/${file}T.py
        COMMAND      -${MYPY}                 ${CMAKE_SOURCE_DIR}/${file}T.py
        COMMAND echo -${PYLINT}               ${CMAKE_SOURCE_DIR}/${file}T.py
        COMMAND      -${PYLINT}               ${CMAKE_SOURCE_DIR}/${file}T.py
        COMMAND echo ${COVERAGE} run --branch ${CMAKE_SOURCE_DIR}/${file}T.py
        COMMAND      ${COVERAGE} run --branch ${CMAKE_SOURCE_DIR}/${file}T.py
        COMMAND echo ${COVERAGE} report -m
        COMMAND      ${COVERAGE} report -m
        DEPENDS .pylintrc)
    add_custom_command (TARGET run
        COMMAND ${MAKE} ${file}T.pyx)
endforeach ()

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES
    ".coverage"
    ".mypy_cache")
