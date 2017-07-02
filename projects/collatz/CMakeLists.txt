cmake_minimum_required (VERSION 3.8.2)

project (Collatz NONE)

enable_testing()

add_custom_command (OUTPUT RunCollatz.tmp COMMAND ../RunCollatz.py < ../RunCollatz.in > RunCollatz.tmp)
add_custom_target  (run ALL DEPENDS RunCollatz.tmp)
add_test           (RunCollatz diff RunCollatz.tmp ../RunCollatz.out)

add_test (TestCollatz ../TestCollatz.py)
