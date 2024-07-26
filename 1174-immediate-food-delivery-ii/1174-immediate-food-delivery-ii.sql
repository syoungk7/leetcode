WITH F AS (SELECT customer_id, order_date,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) as firstorder
    FROM Delivery)
SELECT
  ROUND(SUM(IF(D.order_date = D.customer_pref_delivery_date,1,0)) / COUNT(F.customer_id) *100,2) as immediate_percentage
FROM F
LEFT JOIN Delivery D
ON F.customer_id = D.customer_id AND F.order_date = D.order_date
WHERE F.firstorder = 1;