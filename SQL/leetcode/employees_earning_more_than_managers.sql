/* Write your T-SQL query statement below */

-- plan: join table with itself to find managers

select
e2.name as Employee
-- e2.salary as Employee_Salary,
-- e1.name as Manager,
-- e1.salary as Manager_Salary
from Employee e1
join Employee e2 on e1.id = e2.managerId and e2.salary > e1.salary

-- https://leetcode.com/problems/employees-earning-more-than-their-managers/description/