# Write your MySQL query statement below

# SELECT t.x, t.y, t.z, IF(s.triangle = 1, 'Yes', 'No') AS triangle
# FROM Triangle t, (SELECT x, y, z, 1 AS triangle
#                   FROM Triangle
#                    WHERE x + y > z and x + z > y and y + z > x) s on t.x = s.x 

# SELECT t.x, t.y, t.z, IF(s.triangle is null, 'No', 'Yes') AS triangle
# FROM Triangle t
# LEFT JOIN (SELECT x, y, z, 1 AS triangle
#            FROM Triangle
#            WHERE x + y > z and x + z > y and y + z > x) s on t.x = s.x 

SELECT x, y, z, CASE WHEN (x + y > z and x + z > y and y + z > x) THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle
        
