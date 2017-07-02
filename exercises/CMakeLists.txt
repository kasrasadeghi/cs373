cmake_minimum_required (VERSION 3.8.2)

project (Quizzes NONE)

set (FILES
    UnitTests3T
    Coverage1T
    Coverage2T
    Coverage3T
    IsPrime1T
    IsPrime2T
    FactorialT
    ReduceT
    MapT
    RangeIteratorT
    RangeT
    RMSET
    DecoratorsT
    ComplexT)

enable_testing()

foreach (file ${FILES})
    add_test (${file} ../${file}.py)
endforeach ()
