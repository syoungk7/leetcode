# Write your MySQL query statement below

SELECT MAX(s.num) AS num
FROM (SELECT num
      FROM MyNumbers
      GROUP BY num
      HAVING COUNT(num) = 1) s

# SELECT IF(s.num is null, null, s.num) AS num
# SELECT IFNULL(s.num, null) AS num
# SELECT num
# FROM (SELECT NULLIF(num, NULL) AS num
#       FROM MyNumbers
#       GROUP BY num
#       HAVING COUNT(num) = 1
#       ORDER BY num DESC
#       LIMIT 1) s