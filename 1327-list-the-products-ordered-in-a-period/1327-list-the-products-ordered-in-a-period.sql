# Write your MySQL query statement below
SELECT p.product_name, s.unit
FROM Products p, (SELECT product_id, SUM(unit) AS unit
                  FROM Orders
                  WHERE order_date BETWEEN '2020-02-01' and '2020-02-29'
                  # where left(order_date, 7) = "2020-02"
                  GROUP BY product_id
                  HAVING SUM(unit) >= 100
                 ) s
WHERE p.product_id = s.product_id

# SELECT p.product_name AS product_name, sum(o.unit) AS unit FROM Products p
# JOIN Orders o USING (product_id)
# WHERE YEAR(o.order_date)='2020' AND MONTH(o.order_date)='02'
# GROUP BY p.product_id
# HAVING SUM(o.unit)>=100