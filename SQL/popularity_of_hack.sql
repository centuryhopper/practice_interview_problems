select facebook_employees.location, avg(facebook_hack_survey.popularity) as avg_popularity from facebook_employees
inner join facebook_hack_survey
on facebook_employees.id = facebook_hack_survey.employee_id
-- must have the group by here because of the avg() call above
group by facebook_employees.location

-- https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=1