# Write your MySQL query statement below
# SELECT from_id AS person1, to_id AS person2,
#     COUNT(to_id) AS call_count, 
#     SUM(duration) AS total_duration
# FROM Calls
# GROUP BY from_id, to_id

# SELECT *
# FROM Calls c
# JOIN (SELECT from_id, to_id, SUM(duration) FROM Calls GROUP BY from_id, to_id) t ON (c.from_id, c.to_id) = (t.to_id, t.from_id)

WITH One_direction AS (
    SELECT from_id AS person1, to_id AS person2, duration
    FROM Calls
    WHERE from_id < to_id
    UNION ALL
    SELECT to_id AS person1, from_id AS person2, duration
    FROM Calls
    WHERE from_id > to_id)
    
SELECT person1, person2, 
    COUNT(person1) AS call_count, 
    SUM(duration) AS total_duration
FROM One_direction
GROUP BY person1, person2