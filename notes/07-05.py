# -----------
# Wed,  5 Jul
# -----------

"""
mimic relational algebra in Python
    select
    project
    joins
        cross join
        theta join
        natural join
"""

"""
movie
title, year, director, genre
"shane", 1953, "george stevens", "western"
"star wars", 1977, "george lucas", "western"
...
"""

"""
director
1 "george stevens"
2 "george lucas"
...

movie
title, year, director ID, genre
"shane", 1953, 1, "western"
"star wars", 1977, 2, "western"
...
"""

a = [2, 3, 4]
b = [5, 6, 7]
print(a + b)

a = (2, 3, 4)
b = (5, 6, 7)
print(a + b)

a = {2, 3, 4}
b = {5, 3, 7}
print(a || b)

a = {2:"abc", 3:"def", 4:"ghi"}
b = {5:"abc", 6:"def", 7:"ghi"}
print(dict(a, **b))

def cross_join (r, s) :
    for a in r :
        for b in s :
            yield dict(a, **b)

def cross_join (r, s) :
    return (dict(a, **b) for a in r for b in s)

def theta_join (r, s, bp) :
    for a in r :
        for b in s :
            if bp(a, b)
                yield dict(a, **b)

def theta_join (r, s, bp) :
    return (dict(a, **b) for a in r for b in s if bp(a, b))

































