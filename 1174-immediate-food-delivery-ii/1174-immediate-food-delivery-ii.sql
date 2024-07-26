select round(100*(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(distinct customer_id)), 2) as immediate_percentage
from (select *, row_number() over(partition by customer_id order by order_date) as row_num
from delivery) as grouped_order
where row_num = 1