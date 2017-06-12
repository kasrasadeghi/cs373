# -----------
# Mon, 12 Jun
# -----------

"""
Phase I
    defining the story
    using Apiary do document a RESTful API
    technical report
    static website
    THREE instances of each model

Phase II
    dynamic website
    MANY instances of each model
    implment the API
    a DB backend to render from
    technical report

Phase III
    add search

Phase IV
    add adding, removing, and editing data from the GUI
"""

i = 2
j = 3
k = i + j
k = 2 + 3
(i + j) = 3 # not ok

i + j # not ok

i += j
i += 2
3 += 2 # not ok

k = (i += j) # not ok in Python; is ok in C, C++, Java
(i += j) = 3 # not ok in Python, C, Java; is ok in C++

"""
named variables are examples of l-values
literals are examples of r-values

+  takes two r-values, returns an r-value
+= takes an l-value and an r-value, returns <nothing>

higher-order functions are functions that either take as an argument
or return as a value ANOTHER function
"""

# Java
Integer i = new Integer(2);
Integer j = new Integer(2);
System.out.print(i == j);      # false, identity check
System.out.print(i.equals(u)); # true, content check

# Python
x = [2, 3, 4]
y = [2, 3, 4]
print(x is y) # false, identity check
print(x == y) # true,  content check

"""
+='s RHS is any iterable
"""

i = 2
j = 3
i += j
print(i) # 5
print(j) # 3

i = 2
j = 3
i = i + j
print(i) # 5
print(j) # 3

# for ints: i += j has the same effect as i = i + j
# for lists: x += y does NOT have the same effect as x = x + y

# list's += takes an any iterable
# list's + only takes another list

# tuple's += only takes another tuple
# tuple's +  only takes another tuple

"""
for the mutables
    list
    dict
    set
    x += y IS NOT the same x = x + y


for the immutables
    string
    tuple
    frozenset
    x += y IS the same as x = x + y
"""

# ---------
# Questions
# ---------

"""
What is the l-value/r-value nature of the arguments and the return of the + operator? The += operator?
What is the type of the RHS of list's + operator?
What is the type of the RHS of list's += operator?
What is the type of the RHS of tuple's + operator?
What is the type of the RHS of tuple's += operator?
What is is?
What is ==?
What is a higher-order function?
When is x += y the same as x = x + y?
"""
