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
add_custom_target  (.pylintrcx DEPENDS .pylintrc)
add_test           (.pylintrc  ${MAKE} .pylintrcx)

add_test (Collatz.mypy   ${MYPY}   ../Collatz.py)
add_test (Collatz.pylint ${PYLINT} ../Collatz.py)

add_custom_command (OUTPUT RunCollatz.tmp COMMAND ../RunCollatz.py < ../RunCollatz.in > RunCollatz.tmp)
add_custom_target  (RunCollatz.pyx diff RunCollatz.tmp ../RunCollatz.out DEPENDS RunCollatz.tmp)

add_test (RunCollatz.mypy   ${MYPY}   ../RunCollatz.py)
add_test (RunCollatz.pylint ${PYLINT} ../RunCollatz.py)
add_test (RunCollatz        ${MAKE}      RunCollatz.pyx)

add_custom_command (OUTPUT TestCollatz.tmp COMMAND  ${COVERAGE} run --branch ../TestCollatz.py COMMAND ${COVERAGE} report -m > TestCollatz.tmp)
add_custom_target  (TestCollatz.pyx DEPENDS TestCollatz.tmp)

add_test (TestCollatz.mypy   ${MYPY}   ../TestCollatz.py)
add_test (TestCollatz.pylint ${PYLINT} ../TestCollatz.py)
add_test (TestCollatz        ${MAKE}      TestCollatz.pyx)

set_property (DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES ".coverage" ".mypy_cache")
