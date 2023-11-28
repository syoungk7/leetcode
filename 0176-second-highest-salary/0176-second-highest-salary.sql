# Write your MySQL query statement below
# WITH selected AS (SELECT '2' as ranks, salary
#                 FROM Employee
#                 GROUP BY salary
#                 ORDER BY salary DESC
#                 LIMIT 1 OFFSET 1)

# # SELECT IFNULL((salary), NULL) AS SecondHighestSalary
# # FROM selected

# SELECT e.salary AS SecondHighestSalary
# FROM selected e
# RIGHT JOIN (SELECT '2' as ranks) s ON s.ranks = e.ranks

# SELECT IFNULL((SELECT DISTINCT salary  ## distinct!!
#                 FROM Employee
#                 GROUP BY salary
#                 ORDER BY salary DESC
#                 LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary


SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)