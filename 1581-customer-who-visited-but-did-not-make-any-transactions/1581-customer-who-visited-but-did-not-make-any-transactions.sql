# Write your MySQL query statement below
Select Visits.customer_id, count(Visits.customer_id) as count_no_trans
From Visits
Left Join Transactions 
on Visits.visit_id = Transactions.visit_id
Where Transactions.amount is Null
Group By Visits.customer_id