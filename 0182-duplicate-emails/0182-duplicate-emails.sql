# Write your MySQL query statement below
SELECT email AS Email
FROM Person
GROUP BY email
Having Count(email) != 1