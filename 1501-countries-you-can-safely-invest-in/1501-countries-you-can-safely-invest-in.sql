# Write your MySQL query statement below

SELECT c.name AS country
FROM (SELECT caller_id AS calls, duration
      FROM Calls
      UNION
      SELECT callee_id AS calls, duration
      FROM Calls) t, 
      Person p, Country c
WHERE t.calls = p.id AND LEFT(p.phone_number, 3) = c.country_code
GROUP BY c.name
# HAVING AVG(t.duration) >= (SELECT SUM(duration)/COUNT(2*caller_id) FROM Calls)
HAVING AVG(t.duration) >= (SELECT AVG(duration) FROM Calls)