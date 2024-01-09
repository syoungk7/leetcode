# Write your MySQL query statement below
SELECT t.customer_id, t.name
FROM (SELECT c.customer_id, name, 
            # MONTH(order_date) AS month, 
            IF(SUM(price*quantity)>=100, 1, 0) AS spending
      FROM Customers c, Product p, Orders o
      WHERE c.customer_id = o.customer_id AND p.product_id = o.product_id AND 
            YEAR(order_date)=2020 AND (MONTH(order_date) = 6 OR MONTH(order_date) = 7)
      GROUP BY c.customer_id, MONTH(order_date)) t
GROUP BY t.customer_id
HAVING SUM(spending) = 2