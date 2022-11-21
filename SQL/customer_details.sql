select
    first_name,
    last_name,
    city,
    o.order_details
from customers as c
LEFT JOIN orders as o on c.id = o.cust_id
order by first_name, order_details

-- https://platform.stratascratch.com/coding/9891-customer-details?code_type=1