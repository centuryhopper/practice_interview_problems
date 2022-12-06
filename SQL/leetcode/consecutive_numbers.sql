/* Write your T-SQL query statement below */

-- cartesian join method
select distinct l1.num as ConsecutiveNums 
from Logs l1, Logs l2, Logs l3
where l1.id = l2.id-1 and l2.id = l3.id-1
and l1.num = l2.num and l2.num = l3.num


-- can also use lead and lag as another way to solve this


-- https://leetcode.com/problems/consecutive-numbers/description/