# Write your MySQL query statement below
SELECT person_name
FROM (SELECT person_name, SUM(weight) OVER(ORDER BY turn) AS total_weight
      FROM Queue
      ORDER BY total_weight DESC) s
WHERE total_weight <= 1000
LIMIT 1