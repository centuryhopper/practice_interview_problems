
-- checks to see if there are any duplicate employees (i.e. cnt > 1 rows would be considered having duplicates)
select employeename, Count(employeename) as cnt from sf_public_salaries
group by employeename
order by cnt desc