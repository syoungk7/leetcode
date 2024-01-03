# Write your MySQL query statement below
WITH monthly_spending AS (SELECT c.customer_id, name, 
                            MONTH(order_date) AS month, 
                            SUM(price*quantity) AS spending
                          FROM Customers c
                          inner JOIN Orders o ON c.customer_id = o.customer_id
                          inner JOIN Product p ON p.product_id = o.product_id
                          WHERE YEAR(order_date)=2020 AND (MONTH(order_date) = 6 OR MONTH(order_date) = 7)
                          GROUP BY c.customer_id, name, MONTH(order_date))

SELECT customer_id, name
FROM monthly_spending
GROUP BY customer_id, name
HAVING SUM(IF(spending >= 100, 1, 0)) = 2


# with temp as(
#     select 
#     c.customer_id, c.name, sum(p.price * o.quantity) as price
#     from Customers c
#     inner join 
#     Orders o
#     on c.customer_id = o.customer_id
#     inner join
#     Product p
#     on o.product_id = p.product_id
#     where o.order_date like '2020-06%' or o.order_date like '2020-07%'
#     group by c.customer_id, c.name, month(o.order_date))

# select customer_id, name from temp
# group by customer_id, name
# having sum(case when price >= 100 then 1 else 0 end) = 2
    