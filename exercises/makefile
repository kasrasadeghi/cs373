.DEFAULT_GOAL := all

FILES :=            \
    UnitTests3T     \
    Coverage1T      \
    Coverage2T      \
    Coverage3T      \
    IsPrime1T       \
    IsPrime2T       \
    FactorialT      \
    ReduceT         \
    MapT            \
    RangeIteratorT  \
    RangeT          \
    RMSET           \
    DecoratorsT     \
    ComplexT        \
    SelectT         \
    ProjectT

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    MYPY     := mypy
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

RMSET.pyx: RMSE.py RMSET.py .pylintrc
	-$(MYPY) $<
	-$(PYLINT) $<
	-$(MYPY) $(@:.pyx=.py)
	-$(PYLINT) $(@:.pyx=.py)
	$(PYTHON) $(@:.pyx=.py)

%T.pyx: %.py %T.py .pylintrc
	-$(MYPY) $<
	-$(PYLINT) $<
	-$(MYPY) $(@:.pyx=.py)
	-$(PYLINT) $(@:.pyx=.py)
	$(COVERAGE) run --branch $(@:.pyx=.py)
	$(COVERAGE) report -m

all:

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)

travis:
	make clean
	ls -al
	make test
