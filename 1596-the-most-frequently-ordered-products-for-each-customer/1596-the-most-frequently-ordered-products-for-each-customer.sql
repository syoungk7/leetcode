# Write your MySQL query statement below

# SELECT customer_id, p.product_id, product_name, 
#     SUM() OVER (PARTITION BY (customer_id, o.product_id)) rnk
# FROM Orders o, Products p
# WHERE o.product_id = p.product_id

SELECT customer_id, p.product_id, product_name
FROM (SELECT customer_id, product_id, 
          RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(order_id) DESC) rnk
      FROM Orders
      GROUP BY customer_id, product_id) o, Products p
WHERE o.product_id = p.product_id AND rnk = 1
