.DEFAULT_GOAL := all

FILES :=                    \
    StrategyPattern1        \
    StrategyPattern2        \
    StrategyPattern3        \
    StrategyPattern4        \
    StrategyPattern5        \
    StrategyPattern6

%T.class: %.java %T.java
	javac -Xlint $<
	javac -Xlint $(patsubst %.java,%T.java,$<)

%.class: %.java
	javac -Xlint $<

%T.javax: %.class %T.class
	java -ea $(patsubst %.class,%T,$<)

%.javax: %.class
	java -ea $(patsubst %.class,%,$<)

all: $(FILES:=.class)

clean:
	rm -f *.class

sync:
	make clean
	@echo `pwd`
	@rsync -r -t -u -v --delete \
	--include "makefile"        \
	--include "*.java"          \
	--exclude "*"               \
	. downing@$(CS):cs/patterns/java/

test: $(FILES:=.javax)
