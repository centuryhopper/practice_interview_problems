select location, avg(popularity) avg_popularity from facebook_employees fe
join facebook_hack_survey fhs
on fe.id=fhs.employee_id
group by location

-- https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=1
