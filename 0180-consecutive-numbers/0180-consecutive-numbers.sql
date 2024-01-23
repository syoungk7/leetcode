# Write your MySQL query statement below
SELECT  DISTINCT (l.num) AS ConsecutiveNums
FROM Logs l, logs o, logs g
WHERE l.id = o.id + 1 AND o.id = g.id + 1 AND 
    (l.num = o.num AND o.num = g.num)

