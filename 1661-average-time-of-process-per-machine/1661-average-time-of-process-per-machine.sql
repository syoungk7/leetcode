# Write your MySQL query statement below
SELECT machine_id, ROUND(AVG(pt), 3) AS processing_time
FROM (SELECT machine_id, MAX(timestamp) - MIN(timestamp) AS pt
        FROM Activity
        GROUP BY machine_id, process_id) t
GROUP BY machine_id