/* Write your T-SQL query statement below */

select id, case
    when Tree.p_id is null then 'Root'
    when Tree.id in (select p_id from Tree) then 'Inner'
    else 'Leaf'
end as type
from Tree

-- https://leetcode.com/problems/tree-node/description/?envType=study-plan&id=sql-i