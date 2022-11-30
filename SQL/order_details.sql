select
    c.first_name,
    o.order_date,
    o.order_details,
    o.total_order_cost from customers as c
INNER JOIN orders as o on c.id = o.cust_id
where c.first_name in ('Jill', 'Eva')
order by o.cust_id

-- https://platform.stratascratch.com/coding/9913-order-details?tabname=question
