/* Write your T-SQL query statement below */

select * from Cinema
where id % 2 = 1 and description not like '%boring%'
order by rating desc

-- https://leetcode.com/problems/not-boring-movies/description/
