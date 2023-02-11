select year, sum(south + west + midwest + northeast) from housing_units_completed_us
group by year
order by year



-- https://platform.stratascratch.com/coding/10167-total-number-of-housing-units?code_type=1
