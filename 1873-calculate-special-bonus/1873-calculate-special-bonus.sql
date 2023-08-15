-- Write your MySQL query statement below

Select employee_id, (Case When Mod(employee_id, 2) <> 0 And name Not Like 'M%' 
                     Then salary
                     else 0 
                     end) As bonus
From Employees
Order by employee_id;