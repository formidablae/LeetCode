# Write your MySQL query statement below
select class from (
    select class, COUNT(DISTINCT student) as s
    from courses
    group by class
    ) as cla
where s >= 5
