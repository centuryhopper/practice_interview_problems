/* Write your T-SQL query statement below */

-- | id | recordDate | temperature |
-- | -- | ---------- | ----------- |
-- | 1  | 2000-12-16 | 3           |
-- | 2  | 2000-12-15 | -1          |

-- difference of date by 1 and temperature compare
select w1.id from Weather as w1
join Weather as w2 on
    datediff(day, w2.recordDate, w1.recordDate) = 1
and
    w1.temperature > w2.temperature








