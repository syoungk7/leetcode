# Write your MySQL query statement below
SELECT s.id,
    CASE 
        WHEN s.id%2=1 and a.id is Null THEN s.student
        WHEN s.id%2=1 THEN  a.student
        ELSE e.student
    END AS student
FROM Seat s
LEFT JOIN Seat e ON e.id = s.id - 1
LEFT JOIN Seat a ON a.id = s.id + 1