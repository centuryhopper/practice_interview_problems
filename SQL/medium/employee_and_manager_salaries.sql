with manager_table (id,first_name,employee_title,department,salary,manager_id) as (
    select id,first_name,employee_title,department,salary,manager_id
    from employee
    where employee_title = 'Manager'
),
non_manager_table (id,first_name,employee_title,department,salary,manager_id) as (
    select id,first_name,employee_title,department,salary,manager_id
    from employee
    where employee_title != 'Manager'
)
-- comparing managers' salary with their manager's salary
select m2.first_name, m2.salary as employee_salary from manager_table m1
join manager_table m2
on m1.id = m2.manager_id
where
    m2.id != m2.manager_id
    and
    m2.salary > m1.salary
union all
-- compare employees' salary with their manager's salary
select
nm.first_name as emp_first_name,
nm.salary as employee_salary
from non_manager_table as nm
join manager_table as m
on nm.manager_id = m.id
where m.salary < nm.salary

-- https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?tabname=question