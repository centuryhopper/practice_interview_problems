select e1.department,e1.first_name,e1.salary,sub.avg
from employee e1
INNER JOIN (select department, AVG(salary) as avg from employee
group by department) as sub on e1.department = sub.department

-- https://platform.stratascratch.com/coding/9917-average-salaries?code_type=1