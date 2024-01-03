# Write your MySQL query statement below
WITH monthly_spending AS (SELECT customer_id,
                            # MONTH(order_date) AS month, 
                            SUM(price*quantity) AS spending
                          FROM Orders o, Product p
                          WHERE YEAR(order_date) = 2020 
                            AND (MONTH(order_date) = 6 OR MONTH(order_date) = 7) 
                            AND p.product_id = o.product_id
                          GROUP BY customer_id, MONTH(order_date))

SELECT c.customer_id, name
FROM monthly_spending t, Customers c
WHERE c.customer_id = t.customer_id
GROUP BY c.customer_id, name
HAVING SUM(IF(spending >= 100, 1, 0)) = 2
    