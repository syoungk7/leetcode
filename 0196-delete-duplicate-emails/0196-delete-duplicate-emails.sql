# Write your MySQL query statement below
DELETE
FROM Person 
WHERE (id, email) NOT IN (SELECT * 
                          # FROM Person
                          # GROUP BY email)
                          FROM (SELECT MIN(id), email
                                FROM Person
                                GROUP BY email
                                ORDER BY id) s
                          )