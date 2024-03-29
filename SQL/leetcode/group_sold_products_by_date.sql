# Write your MySQL query statement below
select sell_date, count(distinct product) as num_sold, group_concat(distinct product order by product separator ',') as products from Activities
group by sell_date;

# https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan&id=sql-i