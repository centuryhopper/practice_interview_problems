/* Write your T-SQL query statement below */

select name, sum(amount) as balance
from Users u
join Transactions t on u.account = t.account
group by name
having sum(amount) > 10000

-- https://leetcode.com/problems/bank-account-summary-ii/?envType=study-plan&id=sql-i