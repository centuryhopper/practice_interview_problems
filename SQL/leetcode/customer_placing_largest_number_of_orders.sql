/* Write your T-SQL query statement below */
with counted as (
    select customer_number, count(order_number) as cnt
    from Orders
    group by customer_number
)
select top 1 customer_number from counted
order by cnt desc

-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?envType=study-plan&id=sql-i