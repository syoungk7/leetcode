# Write your MySQL query statement below
# SELECT product_id, (Width*Length*Height) AS volume
# FROM Products

SELECT w.name AS warehouse_name, SUM((w.units*t.prod_volume)) AS volume
FROM Warehouse w, (SELECT product_id, (Width*Length*Height) AS prod_volume
                   FROM Products) t
WHERE w.product_id = t.product_id
GROUP BY w.name