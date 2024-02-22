# Write your MySQL query statement below
SELECT day, emp_id, total_time
FROM (SELECT event_day AS day, emp_id, SUM(out_time-in_time) AS total_time
     FROM Employees
     GROUP BY event_day, emp_id) t
