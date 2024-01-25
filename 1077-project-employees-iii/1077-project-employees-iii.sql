# Write your MySQL query statement below
SELECT project_id, employee_id
FROM (SELECT project_id, p.employee_id, RANK() OVER (PARTITION BY project_id ORDER BY experience_years DESC) rnk
      FROM Project p, Employee e
      WHERE p.employee_id = e.employee_id) t
WHERE rnk = 1