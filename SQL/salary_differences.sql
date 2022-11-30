select
    ABS(
    (select max(salary) from db_employee
    Left JOIN db_dept on db_employee.department_id = db_dept.id
    where db_employee.department_id = 1) -
    (select max(salary) from db_employee
    Left JOIN db_dept on db_employee.department_id = db_dept.id
    where db_employee.department_id = 4)) as salary_difference
-- https://platform.stratascratch.com/coding/10308-salaries-differences?tabname=question