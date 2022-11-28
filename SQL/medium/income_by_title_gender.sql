select employee_title, sex, avg(salary + sb.sum_bonus)
from sf_employee as se
inner join
    (
        select worker_ref_id, sum(bonus) as sum_bonus from sf_bonus
        group by worker_ref_id
    ) as sb
on se.id = sb.worker_ref_id
group by employee_title, sex

-- https://platform.stratascratch.com/coding/10077-income-by-title-and-gender?code_type=1


