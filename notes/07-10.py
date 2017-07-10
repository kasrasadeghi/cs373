# -----------
# Mon, 10 Jul
# -----------

"""
xmllint --noout Bookstore1.xml

XML with DTD
coarse multiplicity with *, +, ?
non-typed pointing system

XML with XSD
fine multiplicity with minOccurs and maxOccurs
typed pointing system

JSON
fine multiplicity with minimum and maximum
NO pointing sytem
"""

"""
movie table
title year director genre
"shane" 1953 "george stevens" "western"
"star wars" 1977 "george lucas" "sci-fi"
"""

"""
director table
id (primary key) name
1 "george stevens"
2 "george lucas"

movie table
title year director-id (foreign key) genre
"shane" 1953 1 "western"
"star wars" 1977 2 "sci-fi"

The InnoDB engine supports foreign keys.
"""

"""
natural join
    no matching attributes degenerates into a cross join
    matching attributes but no matching values produces nothing
    matching attributes and some matching values produces something
"""

# ---------
# Questions
# ---------

"""
What is XML?
What is DTD?
What is XSD?
What makes an XML well-formed?
What makes an XML valid?
What is JSON?
What are foreign keys?
What does it mean to suppor them?
What is inner join?
What is left join?
What is right join?
"""
