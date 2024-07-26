select round(count(d1.customer_id) / (select count(distinct d3.customer_id) from Delivery d3) * 100, 2) as immediate_percentage
from Delivery d1
where d1.order_date =
    (select min(d2.order_date) from Delivery d2 where d1.customer_id = d2.customer_id)
    and d1.order_date = d1.customer_pref_delivery_date