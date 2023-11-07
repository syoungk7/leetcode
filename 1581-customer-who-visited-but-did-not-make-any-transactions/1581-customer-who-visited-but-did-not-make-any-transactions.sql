# Write your MySQL query statement below
# select customer_id, count(customer_id) as count_no_trans
# from Visits
# where visit_id not in (select visit_id from Transactions)
# group by customer_id
# order by count_no_trans Desc

select v.customer_id, count(v.customer_id) as count_no_trans
from Visits v
left join Transactions t on v.visit_id = t.visit_id
where t.amount is Null
group by v.customer_id