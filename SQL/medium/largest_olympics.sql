-- select count(*) from olympics_athletes_events;
select
    distinct games,
    count(distinct name) as athletes_count
from olympics_athletes_events
group by games
order by athletes_count desc
limit 1

-- https://platform.stratascratch.com/coding/9942-largest-olympics?code_type=1
