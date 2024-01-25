# Write your MySQL query statement below
# SELECT name AS customer_name, c.customer_id, order_id, order_date
# FROM Customers c, (SELECT *, RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) rnk
#                   FROM Orders) o
# WHERE c.customer_id = o.customer_id AND (rnk = 1 OR rnk = 2 OR rnk = 3)
# ORDER BY customer_name, c.customer_id, order_date DESC

SELECT name AS customer_name, c.customer_id, order_id, order_date
FROM Customers c, (SELECT *, row_number() OVER (PARTITION BY customer_id ORDER BY order_date DESC) rnk
                  FROM Orders) o
WHERE c.customer_id = o.customer_id AND rnk < 4
ORDER BY customer_name, c.customer_id, order_date DESC


# with cte as(
#     select order_id,  order_date,  o.customer_id as customer_id,  cost, name, 
#         row_number() over(partition by o.customer_id order by order_date desc) as rn
#     from Orders o 
#     left join Customers c
#     on o.customer_id = c.customer_id
# )

# select  name as customer_name, customer_id, order_id,  order_date
# from cte
# where rn <4
# order by name asc, customer_id asc, order_date desc