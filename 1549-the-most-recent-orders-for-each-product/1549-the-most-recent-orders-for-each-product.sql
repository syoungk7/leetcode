# Write your MySQL query statement below
SELECT product_name, p.product_id, order_id, order_date
FROM Products p, (SELECT *, RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) rnk
                  FROM Orders) o
WHERE p.product_id = o.product_id AND rnk = 1
ORDER BY product_name, p.product_id, order_id