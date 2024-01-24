# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, salary
FROM (SELECT *, RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) rnk
     FROM Employee) e, Department d
WHERE e.departmentId = d.id AND rnk = 1