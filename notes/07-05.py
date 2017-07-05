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

print(all([True, 2, 2.5, "a", [2], (2), {2}, {"a": 2}])) # True
print(none([False, 0, 0.0, "", [], (), {}, dict()]))     # False

def theta_join (r, s) :
    def bp (u, v) :
        for k in u :
            if k in v :
                if u[k] != v[k]
                    return False
        return True

    def bp (u, v) :
        return all(u[k] == v[k] for k in u if k in v)

    for a in r :
        for b in s :
            if bp(a, b)
                yield dict(a, **b)

"""
regular expression incredibly valuable
"""

# ---------
# Questions
# ---------

"""
What is cross_join()?
What is theta_join()?
Under what circumstances does theta_join produce nothing?
Under what circumstances does theta_join become cross_join?
What is natural_join()?
Under what circumstances does natural_join produce nothing?
Under what circumstances does natural_join become cross_join?
What is all()?
"""
