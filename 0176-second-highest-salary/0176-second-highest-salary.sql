# Write your MySQL query statement below
# SELECT DISTINCT salary AS SecondHighestSalary
# FROM employee 
# ORDER BY salary DESC 
# LIMIT 1 OFFSET 1

# SELECT IFNULL((SELECT DISTINCT salary 
    # FROM Employee
    # GROUP BY salary
    # ORDER BY salary DESC
    # LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary

SELECT (SELECT DISTINCT salary 
    FROM Employee
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1) AS SecondHighestSalary