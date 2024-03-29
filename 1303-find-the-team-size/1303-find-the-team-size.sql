# Write your MySQL query statement below
SELECT employee_id, team_size
FROM Employee e
JOIN (SELECT team_id, COUNT(team_id) AS team_size
      FROM Employee
      GROUP BY team_id) t ON t.team_id=e.team_id