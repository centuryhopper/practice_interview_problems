
with
table_13 (first_name, target) as (
    select first_name, target from salesforce_employees
    where manager_id = 13
),
max_target (max_target) as (
    select max(target) from table_13
)
select first_name,target from table_13
join max_target on target = max_target

-- https://platform.stratascratch.com/coding/9905-highest-target-under-manager?tabname=question



-- select first_name, target from salesforce_employees
-- where manager_id = 13
-- order by target desc