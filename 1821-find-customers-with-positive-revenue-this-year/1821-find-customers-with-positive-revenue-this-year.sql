# Write your MySQL query statement below
SELECT customer_id
FROM Customers
WHERE year = 2021
GROUP BY customer_id, year
HAVING SUM(revenue) > 0