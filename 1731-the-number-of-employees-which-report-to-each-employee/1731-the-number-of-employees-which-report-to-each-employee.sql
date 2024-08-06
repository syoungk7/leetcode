# Write your MySQL query statement below
SELECT e.employee_id, e.name, s.reports_count, s.average_age
FROM Employees e
JOIN (SELECT reports_to, COUNT(employee_id) AS reports_count, ROUND(AVG(age)) AS average_age
      FROM Employees
      GROUP BY reports_to
      HAVING reports_to is not null) s
      ON e.employee_id = s.reports_to
ORDER BY e.employee_id