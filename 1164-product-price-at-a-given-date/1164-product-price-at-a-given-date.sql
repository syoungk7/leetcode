# Write your MySQL query statement below
SELECT p.product_id, IF(s.max_date is null, 10, new_price) AS price
FROM Products p
LEFT JOIN (SELECT product_id, MAX(change_date) as max_date
           FROM Products
           WHERE change_date <= '2019-08-16'
           GROUP BY product_id) s
        ON p.product_id = s.product_id
WHERE p.change_date = s.max_date or s.max_date is null
GROUP BY p.product_id