# Write your MySQL query statement below




# WITH id_date AS (
#     SELECT a.player_id, c.event_date
#     FROM Activity a, Activity c
#     WHERE a.player_id = c.player_id and DATEDIFF(a.event_date, min_date) = 1
#     GROUP BY a.player_id, c.event_date)


# SELECT ROUND(COUNT(player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
# FROM Activity
# WHERE (player_id, event_date - 1) in (SELECT player_id, MIN(event_date)
#                                       FROM Activity
#                                       GROUP BY player_id)

# SELECT ROUND(num_player/(SELECT COUNT(DISTINCT player_id) 
#                    FROM Activity), 2) AS fraction
# FROM Activity a, selected s
SELECT ROUND(COUNT(a.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a, (SELECT player_id, MIN(event_date) as min_date
                  FROM Activity
                  GROUP BY player_id) s
WHERE a.player_id = s.player_id and DATEDIFF(a.event_date, s.min_date) = 1
