# Write your MySQL query statement below
DELETE 
FROM person 
WHERE (id, email) NOT IN (SELECT id, email
                          FROM (SELECT MIN(id) AS id, email
                                FROM person
                                GROUP BY email) t)

# delete from Person where id not in (select id from (select min(id) as id from Person group by email) as derived_table);