/* Write your T-SQL query statement below */

select emp_id, event_day as day, sum(out_time-in_time) as total_time
from Employees
group by emp_id, event_day


-- https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/?envType=study-plan&id=sql-i