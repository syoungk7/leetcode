# Write your MySQL query statement below
SELECT my.name
FROM
    (SELECT e2.name, COUNT(e1.managerId) as n
    FROM Employee e1 JOIN Employee e2 ON e1.managerId = e2.id
    GROUP BY e1.managerId) my
WHERE n >= 5
