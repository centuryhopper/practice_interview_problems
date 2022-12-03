/* Write your T-SQL query statement below */

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date > '2019-06-27' and activity_date < '2019-07-28'
GROUP BY activity_date

-- OR

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE 0 < datediff(day, activity_date, '2019-07-27') and datediff(day, activity_date, '2019-07-27') < 30
GROUP BY activity_date

-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan&id=sql-i