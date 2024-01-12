# Write your MySQL query statement below
SELECT ABS(p.x-t.x) AS shortest
FROM Point p, Point t
WHERE p.x != t.x
ORDER BY ABS(p.x-t.x)
LIMIT 1