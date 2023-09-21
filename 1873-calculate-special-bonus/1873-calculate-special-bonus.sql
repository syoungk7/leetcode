# Write your MySQL query statement below

Select employee_id,
        If(employee_id % 2 = 1 and name not Like 'M%', salary, 0) as bonus 
From Employees 
Order by employee_id