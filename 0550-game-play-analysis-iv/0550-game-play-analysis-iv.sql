SELECT ROUND(COUNT(a.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a, (SELECT player_id, MIN(event_date) as min_date
                  FROM Activity
                  GROUP BY player_id) s
WHERE a.player_id = s.player_id and DATEDIFF(a.event_date, s.min_date) = 1
