# Write your MySQL query statement below
# SELECT user_id, DATEDIFF('2021-1-1', visit_date)
# FROM UserVisits

WITH temp AS (SELECT user_id, visit_date, 
                LEAD(visit_date) OVER(PARTITION BY user_id ORDER BY visit_date) AS next_visit
              FROM UserVisits)


SELECT user_id, 
    MAX(IF(next_visit IS NULL, 
           DATEDIFF('2021-1-1', visit_date), 
           DATEDIFF(next_visit, visit_date))) AS biggest_window
FROM temp
GROUP BY user_id
