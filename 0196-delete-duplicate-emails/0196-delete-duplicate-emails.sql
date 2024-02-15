# Write your MySQL query statement below
DELETE 
FROM person 
# WHERE (id, email) NOT IN (SELECT id, email
#                           FROM (SELECT MIN(id) AS id, email
WHERE id NOT IN (SELECT id
                          FROM (SELECT MIN(id) AS id
                                FROM person
                                GROUP BY email) t)