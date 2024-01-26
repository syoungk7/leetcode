# Write your MySQL query statement below

# SELECT log_id AS start_id, NUll AS end_id
# FROM (SELECT LAG(log_id) OVER(ORDER BY log_id) AS pre_gap,
#             log_id
#       FROM Logs) t
# WHERE pre_gap IS NULL OR log_id - pre_gap > 1
# UNION 
# SELECT  NUll AS start_id, log_id AS end_id
# FROM (SELECT log_id,
#             LEAD(log_id) OVER(ORDER BY log_id) AS post_gap
#       FROM Logs) t
# WHERE post_gap IS NULL OR post_gap - log_id > 1


SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM (SELECT ROW_NUMBER() OVER(ORDER BY log_id) AS pre_gap,
            log_id
      FROM Logs) t
GROUP BY log_id-pre_gap
ORDER BY start_id