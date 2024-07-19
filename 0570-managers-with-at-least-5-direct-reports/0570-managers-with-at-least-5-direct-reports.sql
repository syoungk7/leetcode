# Write your MySQL query statement below
select e.name from employee e
where e.id in
(select managerId from employee
where managerId is not null
group by managerId
having count(*) >= 5)