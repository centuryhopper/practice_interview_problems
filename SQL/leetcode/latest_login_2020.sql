/* Write your T-SQL query statement below */


select user_id, max(time_stamp) as last_stamp from Logins
where year(time_stamp) = 2020
group by user_id

-- https://leetcode.com/problems/the-latest-login-in-2020/?envType=study-plan&id=sql-i