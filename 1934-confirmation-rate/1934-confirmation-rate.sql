# Write your MySQL query statement below
SELECT s.user_id, COALESCE(ROUND(AVG(actnum), 2), 0) AS confirmation_rate
FROM Signups s
LEFT JOIN (SELECT *,
                CASE
                    WHEN action = 'timeout' THEN 0
                    WHEN action = 'confirmed' THEN 1
                END AS actnum
            FROM Confirmations) as my
ON s.user_id = my.user_id
GROUP BY s.user_id