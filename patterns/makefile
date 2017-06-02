.DEFAULT_GOAL := test

FILES :=

FactoryMethodPatternT.class: FactoryMethodPattern.java FactoryMethodPatternT.java
	javac -Xlint FactoryMethodPattern.java
	javac -Xlint FactoryMethodPatternT.java

SingletonPatternT.class: SingletonPattern.java SingletonPatternT.java
	javac -Xlint SingletonPattern.java
	javac -Xlint SingletonPatternT.java

%.class: %.java
	javac -Xlint $<

%.javax: %.class
	java -ea $(patsubst %.class,%,$<)

clean:
	rm -f *.class

test: $(FILES:=.javax)
