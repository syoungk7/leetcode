SELECT ROUND(COUNT(a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a
    LEFT JOIN (SELECT player_id, MIN(event_date) AS first_login
    FROM Activity GROUP BY player_id) my
    ON a.player_id = my.player_id
WHERE event_date = first_login + INTERVAL 1 DAY