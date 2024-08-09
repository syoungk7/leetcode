# Write your MySQL query statement below
WITH ONE as (
    SELECT employee_id, count(employee_id) as ce
    FROM Employee
    GROUP BY employee_id)

SELECT E.employee_id, E.department_id
    # CASE
    #     WHEN ONE.ce = 1 THEN E.department_id
    #     WHEN E.primary_flag = 'Y' THEN E.department_id
    #     ELSE 0
    # END AS department_id
FROM Employee E
JOIN ONE ON E.employee_id = ONE.employee_id
Where primary_flag = 'Y' or ONE.ce = 1