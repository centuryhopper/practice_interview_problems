# Write your MySQL query statement below

select user_id,
concat(upper(substr(Users.name,1,1)),lower(substr(Users.name,2))) as name
from Users
order by user_id;

# strings are 1 indexed in SQL

# https://leetcode.com/problems/fix-names-in-a-table/description/
