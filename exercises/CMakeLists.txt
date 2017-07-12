cmake_minimum_required (VERSION 3.8.2)

project (Exercises NONE)

find_program(COVERAGE coverage)
message(${COVERAGE})

find_program (MAKE make)
message(${MAKE})

find_program (MYPY mypy)
message(${MYPY})

find_program (PYLINT pylint)
message(${PYLINT})

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
    RMSE
    Decorators
    Complex)

enable_testing ()

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)
add_custom_target  (.pylintrcx DEPENDS .pylintrc)
add_test           (.pylintrc  ${MAKE} .pylintrcx)

foreach (file ${FILES})
    add_custom_command (OUTPUT ${file}.cov COMMAND ${COVERAGE} report -m > ${file}T.cov)
    add_custom_target  (${file}.covx DEPENDS ${file}.cov)

    add_test (${file}.mypy   ${MYPY}                  ../${file}.py)
    add_test (${file}.pylint ${PYLINT}                ../${file}.py)
    add_test (${file}.mypy   ${MYPY}                  ../${file}T.py)
    add_test (${file}.pylint ${PYLINT}                ../${file}T.py)
    add_test (${file}        ${COVERAGE} run --branch ../${file}T.py)
    add_test (${file}.cov    ${MAKE}                     ${file}.covx)
endforeach ()

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES ".coverage" ".mypy_cache")
