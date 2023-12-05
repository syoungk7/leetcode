# Write your MySQL query statement below
SELECT s.requester_id AS id, COUNT(s.requester_id) AS num
FROM  (
    (SELECT accepter_id AS requester_id, requester_id AS accepter_id, accept_date
     FROM RequestAccepted)
    UNION ALL 
    (SELECT *
     FROM RequestAccepted)
    ) s
GROUP BY s.requester_id
ORDER BY COUNT(s.requester_id) DESC
LIMIT 1