# Write your MySQL query statement below
with unioned as (
  select Employees.employee_id, name, salary from Employees
  left join Salaries
  on Salaries.employee_id = Employees.employee_id
  union all
  select Salaries.employee_id, name, salary from Employees
  right join Salaries
  on Salaries.employee_id = Employees.employee_id
)
select employee_id from unioned
where name is null or salary is null
order by employee_id;

# https://leetcode.com/problems/employees-with-missing-information/description/?envType=study-plan&id=sql-i