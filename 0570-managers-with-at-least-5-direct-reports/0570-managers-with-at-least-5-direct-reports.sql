# Write your MySQL query statement below
select name
from Employee
where id in (select managerId
             from Employee
             group by managerId
             having count(managerId) >= 5)
# select e.name
# from Employee e
# join (select managerId
#       from Employee
#       group by managerId
#       having count(managerId) >= 5) m on e.id = m.managerId