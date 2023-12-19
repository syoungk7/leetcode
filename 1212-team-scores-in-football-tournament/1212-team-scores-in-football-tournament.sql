# Write your MySQL query statement below

WITH Team_goals AS (
    SELECT host_team AS team, host_goals AS h_gals, guest_goals AS g_goals
    FROM Matches
    UNION ALL
    SELECT guest_team AS team, guest_goals AS h_gals, host_goals AS g_goals
    FROM Matches)
, Team_points AS (
    SELECT team, SUM(IF(h_gals > g_goals, 3, IF(h_gals = g_goals, 1, 0))) AS points
    FROM Team_goals
    GROUP BY team
    )

SELECT team_id, team_name, IFNULL(t.points, 0) AS num_points
FROM Teams
LEFT JOIN Team_points t ON team_id = t.team
ORDER BY num_points DESC, team_id ASC


 