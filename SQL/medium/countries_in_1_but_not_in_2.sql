select country from winemag_p1
where country not in (select country from winemag_p2)
order by country

-- https://platform.stratascratch.com/coding/10147-find-countries-that-are-in-winemag_p1-dataset-but-not-in-winemag_p2?code_type=1
