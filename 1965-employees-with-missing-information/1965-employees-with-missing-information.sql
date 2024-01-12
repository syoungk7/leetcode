# Write your MySQL query statement below
SELECT t.employee_id
FROM (SELECT s.employee_id, e.name, s.salary
      FROM Employees e
      RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
      UNION
      SELECT e.employee_id, e.name, s.salary
      FROM Employees e
      LEFT JOIN Salaries s ON e.employee_id = s.employee_id) t
WHERE t.name IS NULL or t.salary IS NULL
ORDER BY t.employee_id