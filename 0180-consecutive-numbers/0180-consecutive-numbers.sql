# Write your MySQL query statement below
SELECT  DISTINCT (l.num) AS ConsecutiveNums
FROM Logs l, logs o, logs g
WHERE l.id = o.id + 1 AND o.id = g.id + 1 AND 
    (l.num = o.num AND o.num = g.num)
    
# SELECT DISTINCT l1.num as ConsecutiveNums
# FROM Logs l1 
# JOIN Logs l2 ON (l1.id = l2.id-1 AND l1.num=l2.num)
# JOIN Logs l3 ON (l2.id = l3.id-1 AND l2.num=l3.num)