# Write your MySQL query statement below

SELECT DISTINCT p.product_id, IF(t.max_date IS NOT NULL, p.new_price, 10) AS price
FROM Products p
LEFT JOIN (SELECT product_id, MAX(change_date) as max_date
           FROM Products
           WHERE change_date <= '2019-08-16'
           GROUP BY product_id) t 
    ON t.product_id = p.product_id

WHERE p.change_date = t.max_date or t.max_date is null
GROUP BY product_id
