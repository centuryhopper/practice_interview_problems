
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

select distinct city from station
where 
city like '%a' or
city like '%e' or
city like '%i' or
city like '%o' or
city like '%u';

-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true







