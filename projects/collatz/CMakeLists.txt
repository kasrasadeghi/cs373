cmake_minimum_required (VERSION 3.8.2)

project (Collatz NONE)

find_program(COVERAGE coverage)
message(${COVERAGE})

find_program (MAKE make)
message(${MAKE})

find_program (MYPY mypy)
message(${MYPY})

find_program (PYLINT pylint)
message(${PYLINT})

enable_testing ()

add_custom_command (OUTPUT .pylintrc COMMAND ${PYLINT} --disable=locally-disabled --reports=no --generate-rcfile > .pylintrc)
add_custom_target  (.pylintrcx ALL DEPENDS .pylintrc)

add_custom_command (OUTPUT RunCollatz.tmp COMMAND ../RunCollatz.py < ../RunCollatz.in > RunCollatz.tmp)
add_custom_target (RunCollatz.tmpx ALL DEPENDS RunCollatz.tmp)

add_test (Collatz.mypy       ${MYPY}                  ../Collatz.py)
add_test (Collatz.pylint     ${PYLINT}                ../Collatz.py)

add_test (RunCollatz.mypy    ${MYPY}                  ../RunCollatz.py)
add_test (RunCollatz.pylint  ${PYLINT}                ../RunCollatz.py)
add_test (RunCollatz         diff RunCollatz.tmp      ../RunCollatz.out)

add_custom_command (OUTPUT TestCollatz.cov COMMAND ${COVERAGE} report -m > TestCollatz.cov)
add_custom_target  (TestCollatz.covx DEPENDS TestCollatz.cov)

add_test (TestCollatz.mypy   ${MYPY}                  ../TestCollatz.py)
add_test (TestCollatz.pylint ${PYLINT}                ../TestCollatz.py)
add_test (TestCollatz        ${COVERAGE} run --branch ../TestCollatz.py)
add_test (${file}.cov        ${MAKE}                     TestCollatz.covx)

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES ".coverage" ".mypy_cache")

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
