/* Write your T-SQL query statement below */

with joined as
(
    select s.name as person_name, c.name as company_name
    from SalesPerson s
    left join Orders o on s.sales_id = o.sales_id
    left join Company c on c.com_id = o.com_id
),
agg as
(
    select person_name, STRING_AGG(joined.company_name ,';') as concatted
    from joined
    group by person_name
    having STRING_AGG(joined.company_name ,';') not LIKE '%RED%' or STRING_AGG(joined.company_name ,';') is null
)
select person_name as name from agg

-- https://leetcode.com/problems/sales-person/description/?envType=study-plan&id=sql-i



