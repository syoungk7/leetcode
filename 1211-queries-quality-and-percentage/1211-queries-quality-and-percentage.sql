# Write your MySQL query statement below
SELECT query_name,
    ROUND(AVG(rating/position), 2) AS quality,
    ROUND(SUM(IF(rating < 3, 1, 0))/COUNT(query_name)*100, 2) AS poor_query_percentage
FROM Queries
Where query_name is not null
GROUP BY query_name