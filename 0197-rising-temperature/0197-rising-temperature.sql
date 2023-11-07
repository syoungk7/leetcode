# Write your MySQL query statement below
select w.id
from Weather w
Join Weather e on DATEDIFF(w.recordDate, e.recordDate) = 1 and w.temperature - e.temperature > 0
