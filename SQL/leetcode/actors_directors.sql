/* Write your T-SQL query statement below */


select actor_id, director_id
from ActorDirector
group by actor_id, director_id
-- asterisk here applys to the rest of the columns
-- not mentioned in the select. In this case, it's
-- just timestamp
having count(*) >= 3

-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/?envType=study-plan&id=sql-i