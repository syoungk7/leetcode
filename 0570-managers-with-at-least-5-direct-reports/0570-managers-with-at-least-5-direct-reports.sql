# Write your MySQL query statement below
select e1.name
from employee as e1, (select managerId
from employee
group by managerId
having count(*) >= 5) as e2
where e1.id = e2.managerId