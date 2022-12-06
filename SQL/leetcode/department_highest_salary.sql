/* Write your T-SQL query statement below */


with joined as
(
    select e.name,
    e.salary as emp_sal,
    d.name as Department,
    max(salary) over(partition by d.name) as Salary
    from Employee e
    join Department d on e.departmentId = d.id
)
select name as Employee, Department, Salary from joined
where Salary = emp_sal

-- https://leetcode.com/problems/department-highest-salary/




