select ah.nationality, count(distinct au.unit_id) as cnt from airbnb_hosts as ah
inner join airbnb_units as au
on ah.host_id = au.host_id
where ah.age < 30 and lower(au.unit_type) = 'apartment'
group by ah.nationality
order by cnt desc

-- https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=1