/* Write your T-SQL query statement below */

-- https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan&id=sql-i

with store1Group as
(
    select product_id, store1 as price,
    case
        when store1 is not null then 'store1'
    end as store
    from Products
),
store2Group as
(
    select product_id, store2 as price,
    case
        when store2 is not null then 'store2'
    end as store
    from Products
),
store3Group as
(
    select product_id, store3 as price,
    case
        when store3 is not null then 'store3'
    end as store
    from Products
),
unioned as
(
    select * from store1Group
    union all
    select * from store2Group
    union all
    select * from store3Group
)
select * from unioned
where price != 0 or price is not null

