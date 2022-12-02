/* Write your T-SQL query statement below */

with joined as
(
    select customer_id,transaction_id from Visits as v
    left join Transactions as t
    on v.visit_id = t.visit_id
),
getNullsAndNonNulls as
(
    select
        customer_id,
        count(*)-count(transaction_id) as nulls,
        count(transaction_id) as nonnulls
    from joined
    group by customer_id
)
select customer_id, nulls as count_no_trans
from getNullsAndNonNulls
where nulls > 0

-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan&id=sql-i







