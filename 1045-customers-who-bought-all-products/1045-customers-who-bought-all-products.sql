# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)
# HAVING SUM(IF(DISTINCT product_key IN (SELECT product_key FROM Product), 1, 0)) = (SELECT COUNT(product_key) FROM Product)