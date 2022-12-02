/* Write your T-SQL query statement below */

WITH
removedDupes as
(
    select distinct salary from Employee
),
salaries AS
(
    SELECT salary,
    ROW_NUMBER() OVER (ORDER BY salary desc) as RowNumber
    FROM removedDupes
),
result as
(
    SELECT salary
    FROM salaries
    WHERE RowNumber = 2
)
-- places a null in there if its null
select (select * from result) as SecondHighestSalary

-- select * from removedDupes





