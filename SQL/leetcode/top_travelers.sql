/* Write your T-SQL query statement below */

-- | id | name  |
-- | -- | ----- |
-- | 1  | Alice |
-- | 2  | Bob   |
-- | 3  | Alex  |
-- | 19 | Alice |

-- | id | user_id | distance |
-- | -- | ------- | -------- |
-- | 1  | 1       | 120      |
-- | 2  | 2       | 317      |
-- | 3  | 3       | 222      |
-- | 4  | 7       | 100      |
-- | 5  | 13      | 312      |
-- | 9  | 7       | 230      |

with joined as
(
    select u.id, name, case
        when distance is null then 0
        else distance
    end as travelled_distance
    from Users u
    left join Rides r on u.id = r.user_id
),
summarize as
(
    select name, id, sum(travelled_distance) as travelled_distance
    from joined
    group by name, id
)
select name, travelled_distance
from summarize
order by travelled_distance desc, name

-- https://leetcode.com/problems/top-travellers/description/?envType=study-plan&id=sql-i
