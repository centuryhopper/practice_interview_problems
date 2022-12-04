/* Write your T-SQL query statement below */

with processed_orders as
(
    select buyer_id, count(order_date) as orders_in_2019
    from Orders
    where year(order_date) = 2019
    group by buyer_id
),
joined as
(
    select user_id, join_date, orders_in_2019
    from Users u
    left join processed_orders p on u.user_id = p.buyer_id
)
select user_id as buyer_id, join_date, isnull(orders_in_2019, 0) as orders_in_2019
from joined

-- https://leetcode.com/problems/market-analysis-i/description/





