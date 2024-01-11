# Write your MySQL query statement below
# SELECT player_id, MIN(event_date) AS min_date
# FROM Activity
# GROUP BY player_id

SELECT ROUND(SUM(IF(DATEDIFF(a.event_date, t.min_date)=1, 1, 0))/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM Activity a, (SELECT player_id, MIN(event_date) AS min_date
                  FROM Activity
                  GROUP BY player_id) t
WHERE a.player_id = t.player_id