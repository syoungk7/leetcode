# Write your MySQL query statement below
SELECT DISTINCT(c.seat_id)
FROM Cinema c, Cinema t
WHERE (c.seat_id-1=t.seat_id OR c.seat_id+1=t.seat_id) and (c.free = 1 and t.free = 1)
ORDER BY c.seat_id