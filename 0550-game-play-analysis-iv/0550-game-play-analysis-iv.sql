SELECT
    ROUND(SUM(CASE WHEN first_date + INTERVAL 1 DAY = event_date THEN 1 ELSE 0 END) / COUNT(distinct A.player_id),2) as fraction
FROM ( SELECT player_id, min(event_date) as first_date
      FROM Activity
      GROUP BY player_id) X
JOIN Activity A
ON X.player_id = A.player_id;