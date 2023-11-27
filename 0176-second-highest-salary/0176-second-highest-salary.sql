# Write your MySQL query statement below


# SELECT IFNULL((salary), NULL) AS SecondHighestSalary
# FROM selected

SELECT e.salary AS SecondHighestSalary
FROM (SELECT '2' as ranks, salary
      FROM Employee
      GROUP BY salary
      ORDER BY salary DESC
      LIMIT 1 OFFSET 1) e
RIGHT JOIN (SELECT '2' as ranks) s ON s.ranks = e.ranks

# SELECT IFNULL((SELECT salary
#                 FROM Employee
#                 GROUP BY salary
#                 ORDER BY salary DESC
#                 LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
