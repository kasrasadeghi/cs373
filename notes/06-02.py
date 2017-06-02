# ----------
# Fri, 2 Jun
# ----------

"""
please e-mail via Canvas for personal issue
not personal, use Piazza

continuous integration

value of testing

1. getting clarity about what you're about to code
2. having tests to validate the code you wrote
3. in the future you'll have a set of regression tests

two qualities of testing

1. how much of the code is actually being tested
   we can use a coverage tool to find out

2. you have to run the tests

continuous integration a system that listens to git commits, then automatically spins a VM and runs the tests

two qualities of continuous integration

1. the tests are sure to be run

2. makes explicit dependencies that your code or tests might have

JavsScript is optional
advice: look into TypeScript

first third: intro to Python
second third: XML, JSON, relational algebra, SQL
third third: refactoring, design patterns, in Java

nice to be confident a consistent environment between you and your team mates when writing group code

Docker / DockerHub very nice way of defining a consistent environment for a team
"""

def f (i: int) :
    ...

"""
intro to Docker
intro to Travis CI

simple script in Python

help system in Python

three ways to run a script

1. python3 <name of script>
2. mark the script executable and have special first line
   script is self-executing
3. enter Python and use import

very important to avoid errors in coding

two types of errors

1. compile time
2. runtime

two types of errors

1. programmer errors
2. user errors

intro assertions

1. good for programmer errors, not good for user errors
2. not good for unit testing

Collatz Conjecture

take a pos int
if even divide by 2
else multiply by 3 and add 1
repeat until 1

5 16 8 4 2 1

cycle length of 5 is 6
cycle length of 10 is 7

5 /  2 -> 2.5
5 // 2 -> 2

5.0 /  2 -> 2.5
5.0 // 2 -> 2.0
"""
