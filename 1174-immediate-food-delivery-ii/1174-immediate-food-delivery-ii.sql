# Write your MySQL query statement below

# SELECT ROUND(SUM(IF((d.order_date = d.customer_pref_delivery_date), 1, 0))/COUNT(d.customer_id)*100, 2) AS immediate_percentage
SELECT ROUND(AVG(IF(s.min_date = d.customer_pref_delivery_date, 1, 0))*100, 2) AS immediate_percentage
FROM Delivery d
JOIN (SELECT customer_id, MIN(order_date) AS min_date
      FROM Delivery
      GROUP BY customer_id) s 
ON d.order_date = s.min_date and d.customer_id = s.customer_id

# WHERE (customer_id, order_date) IN (SELECT customer_id, MIN(order_date) AS min_date
#                                     FROM Delivery
#                                     GROUP BY customer_id)