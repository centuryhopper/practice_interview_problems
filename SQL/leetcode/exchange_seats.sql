/* Write your T-SQL query statement below */

with indexed as
(
    select *,
    count(id) over() as n_rows,
    row_number() over(order by id) as row_number,
    lead(student) over(order by id) as next,
    lag(student) over(order by id) as prev
    from Seat
)
-- select * from indexed
select id, case
    when row_number = n_rows and row_number % 2 = 1 then student
    when row_number % 2 = 1 then next
    when row_number % 2 = 0 then prev
end as student
from indexed

-- https://leetcode.com/problems/exchange-seats/description/

