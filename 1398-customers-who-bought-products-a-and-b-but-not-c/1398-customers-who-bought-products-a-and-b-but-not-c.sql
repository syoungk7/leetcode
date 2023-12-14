# Write your MySQL query statement below
WITH Counting AS (SELECT t.customer_id, 
                    CASE t.product_name
                        WHEN 'A' THEN 1
                        WHEN 'B' THEN 1
                        WHEN 'C' THEN -1
                        ELSE 0
                    END AS tmp_count
                  FROM (SELECT customer_id, product_name
                        FROM Orders
                        GROUP BY customer_id, product_name) t
                 )
# # SELECT *
# # FROM Counting
SELECT o.customer_id, c.customer_name
FROM Counting o, Customers c
WHERE o.customer_id = c.customer_id
GROUP BY o.customer_id
HAVING SUM(o.tmp_count) = 2