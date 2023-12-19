# Write your MySQL query statement below

# WITH Team_goals AS (
#     SELECT host_team AS team, host_goals AS h_gals, guest_goals AS g_goals
#     FROM Matches
#     UNION ALL
#     SELECT guest_team AS team, guest_goals AS h_gals, host_goals AS g_goals
#     FROM Matches)
# , Team_points AS (
#     SELECT team, SUM(IF(h_gals > g_goals, 3, IF(h_gals = g_goals, 1, 0))) AS points
#     FROM Team_goals
#     GROUP BY team
#     )

# SELECT team_id, team_name, IFNULL(SUM(3*(host_goals>guest_goals) + (host_goals=guest_goals)), 0) AS num_points
# FROM Teams
# LEFT JOIN (SELECT * FROM Matches
#      UNION ALL
#      SELECT match_id, guest_team, host_team, guest_goals, host_goals 
#      FROM Matches) t ON team_id = t.host_team
# GROUP BY team_id
# ORDER BY num_points DESC


SELECT 
    team_id, 
    team_name, 
    IFNULL(SUM(3*(host_goals>guest_goals) + (host_goals=guest_goals)), 0) AS num_points
FROM 
    Teams 
LEFT JOIN 
    (SELECT * FROM Matches
     UNION ALL
     SELECT match_id, guest_team, host_team, guest_goals, host_goals 
     FROM Matches) a ON team_id = host_team 
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC; 