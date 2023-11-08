# Write your MySQL query statement below
select a.machine_id, round(sum((c.timestamp - a.timestamp))/count(a.process_id), 3) as processing_time
from Activity a
join Activity c on a.machine_id = c.machine_id and a.process_id = c.process_id and a.activity_type = 'start' and c.activity_type = 'end'
group by a.machine_id