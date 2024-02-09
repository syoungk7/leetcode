# Write your MySQL query statement below
SELECT 'bull' AS word, SUM(IF(content REGEXP ' bull ', 1, 0)) AS count 
FROM files
UNION 
SELECT 'bear' AS word, SUM(IF(content REGEXP ' bear ', 1, 0)) AS count 
FROM files