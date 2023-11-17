# Write your MySQL query statement below
# WITH selected AS (SELECT '2' as ranks, salary
#                 FROM Employee
#                 GROUP BY salary
#                 ORDER BY salary DESC
#                 LIMIT 1 OFFSET 1)

# SELECT e.salary AS SecondHighestSalary
# FROM selected e
# RIGHT JOIN (SELECT '2' as ranks) s ON s.ranks = e.ranks

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary