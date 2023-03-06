select cast(sum(lat_n) as decimal(10,2)) lat,
cast(sum(long_w) as decimal(10,2)) long
from station;

-- https://www.hackerrank.com/challenges/weather-observation-station-2/problem
