# -----------
# Wed, 12 Jul
# -----------

"""
*: zero or more
+: one  or more
?: zero or one
"""

select sID, sName, GPA
    from Student inner join Apply using (sID)
    where major = 'CS'

select distinct GPA
    from Student inner join Apply using (sID)
    where major = 'CS'

select sID
    from Student
    where
    sID in (select sID from Apply where major = 'CS')
    and
    sID not in (select sID from Apply where major = 'EE')

select *
    from College as C
    where
        select *
        from College as T
        where C.cName != T.cName
        and   C.state =  T.state

select *
    from College as C1
    where not exists
        (select *
        from College as C2
        where C1.enrollment < C2.enrollment)

# ---------
# Questions
# ---------

"""
What is a subquery? When is it useful?
When is it useful to join a table with itself?
What is group by?
What is having?
"""
