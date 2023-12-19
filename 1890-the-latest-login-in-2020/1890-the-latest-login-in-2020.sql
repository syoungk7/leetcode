# Write your MySQL query statement below

WITH year_rank AS (SELECT user_id, time_stamp, 
                   RANK () OVER (PARTITION BY user_id ORDER BY user_id, time_stamp DESC) AS ranks
                   FROM Logins
                   WHERE YEAR(time_stamp) = 2020
                   ORDER BY user_id, time_stamp DESC
                  )

                   
SELECT user_id, time_stamp AS last_stamp
FROM year_rank
WHERE ranks = 1
