# Write your MySQL query statement below
SELECT p.product_name, s.unit
FROM Products p, (SELECT product_id, SUM(unit) AS unit
                  FROM Orders
                  WHERE order_date BETWEEN '2020-02-01' and '2020-02-29'
                  GROUP BY product_id
                  HAVING SUM(unit) >= 100
                 ) s
WHERE p.product_id = s.product_id

