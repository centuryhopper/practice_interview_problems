/* Write your T-SQL query statement below */

with joined as
(
    select p.product_id, product_name, sale_date, case
        when sale_date between '2019-01-01' and '2019-03-31' then 'good'
        else 'bad'
    end as flag
    from Product p
    join Sales s on p.product_id = s.product_id
)
select product_id, product_name
from joined
group by product_id, product_name
having STRING_AGG(flag ,';') not like '%bad%'

-- https://leetcode.com/problems/sales-analysis-iii/?envType=study-plan&id=sql-i
