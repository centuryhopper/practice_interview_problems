select bike_number, max(end_time) as last_used from dc_bikeshare_q1_2012
group by bike_number
order by last_used desc;

-- aggregates functions like max() need a group by thats why we have one here
