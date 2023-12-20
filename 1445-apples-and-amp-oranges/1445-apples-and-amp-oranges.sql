# Write your MySQL query statement below
SELECT s.sale_date, (s.sold_num-t.ora_nums) AS diff
FROM Sales s
LEFT JOIN (SELECT sale_date, fruit AS oranges, sold_num AS ora_nums
           FROM Sales 
           WHERE fruit = 'oranges') t 
    ON (s.sale_date = t.sale_date)
WHERE fruit = 'apples'
ORDER BY sale_date