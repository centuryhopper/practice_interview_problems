/* Write your T-SQL query statement below */

with summarize_buy as
(
    select stock_name, sum(price) as total_buy_price
    from Stocks
    where operation = 'Buy'
    group by stock_name
),
summarize_sell as
(
    select stock_name, sum(price) as total_sell_price
    from Stocks
    where operation = 'Sell'
    group by stock_name
)
select buy.stock_name, (total_sell_price - total_buy_price) as capital_gain_loss
from summarize_buy buy
join summarize_sell sell
on buy.stock_name = sell.stock_name

-- https://leetcode.com/problems/capital-gainloss/description/?envType=study-plan&id=sql-i

