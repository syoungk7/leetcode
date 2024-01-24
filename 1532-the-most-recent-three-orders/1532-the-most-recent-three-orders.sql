# Write your MySQL query statement below
SELECT name AS customer_name, c.customer_id, order_id, order_date
FROM Customers c, (SELECT *, RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) rnk
                  FROM Orders) o
WHERE c.customer_id = o.customer_id AND (rnk = 1 OR rnk = 2 OR rnk = 3)
ORDER BY customer_name, c.customer_id, order_date DESC