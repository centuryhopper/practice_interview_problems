/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem
select distinct city from station
where 
city like 'a%' or
city like 'e%' or
city like 'i%' or
city like 'o%' or
city like 'u%';

