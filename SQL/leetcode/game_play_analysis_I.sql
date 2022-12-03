/* Write your T-SQL query statement below */

select player_id, min(event_date) as first_login from Activity
group by player_id

-- https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan&id=sql-i