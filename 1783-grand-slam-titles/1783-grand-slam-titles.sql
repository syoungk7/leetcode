# Write your MySQL query statement below
WITH games AS (SELECT Wimbledon AS game
               FROM Championships
               UNION ALL
               SELECT Fr_open AS game
               FROM Championships
               UNION ALL
               SELECT US_open AS game
               FROM Championships
               UNION ALL
               SELECT Au_open AS game
               FROM Championships)
               
SELECT p.player_id, p.player_name, COUNT(g.game) AS grand_slams_count
FROM games g, Players p
WHERE p.player_id = g.game
GROUP BY g.game