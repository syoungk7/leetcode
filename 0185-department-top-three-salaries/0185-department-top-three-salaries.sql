# Write your MySQL query statement below
WITH salary_order AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary, 
        DENSE_RANK () OVER (PARTITION BY d.id ORDER BY e.salary DESC) salary_rank
    FROM Employee e, Department d
    WHERE e.departmentId = d.id
    )

SELECT Department, Employee, salary
FROM salary_order
WHERE salary_rank <= 3

