cmake_minimum_required (VERSION 3.8.2)

project (Exercises NONE)

find_program(COVERAGE coverage)
find_program(MYPY     mypy)
find_program(PYLINT   pylint)

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

set_directory_properties (PROPERTIES ADDITIONAL_MAKE_CLEAN_FILES ".coverage")

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)

add_custom_target (.pylintrcx ALL DEPENDS .pylintrc)

enable_testing()

foreach (file ${FILES})
    add_test (${file}.mypy   ${MYPY}                  ../${file}.py)
    add_test (${file}.pylint ${PYLINT}                ../${file}.py)
    add_test (${file}.mypy   ${MYPY}                  ../${file}T.py)
    add_test (${file}.pylint ${PYLINT}                ../${file}T.py)
    add_test (${file}        ${COVERAGE} run --branch ../${file}T.py)
    add_test (${file}.cov    ${COVERAGE} report -m)
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
