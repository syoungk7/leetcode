# Write your MySQL query statement below
SELECT MAX(s.num) AS num
FROM (SELECT num
      FROM MyNumbers
      GROUP BY num
      HAVING COUNT(num) = 1) s
#ORDER BY num DESC
#LIMIT 1