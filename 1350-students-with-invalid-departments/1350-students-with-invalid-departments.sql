# Write your MySQL query statement below
SELECT s.id, s.name
FROM Students s
LEFT JOIN Departments d
    ON d.id = s.department_id
WHERE d.name IS NULL