/* Write your T-SQL query statement below */

with dupes as
(
    select email,
    count(id) as cnt
    from Person
    group by email
)
select email from dupes
where cnt > 1

-- https://leetcode.com/problems/duplicate-emails/?envType=study-plan&id=sql-i