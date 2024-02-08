# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id=viewer_id AND author_id IN (SELECT DISTINCT viewer_id FROM Views)
ORDER BY author_id