# Write your MySQL query statement below
WITH ranking AS (
    SELECT student_id, course_id, grade,
        RANK() OVER (PARTITION BY student_id ORDER BY grade DESC) AS ranks
    FROM Enrollments
    ORDER BY student_id, course_id)

SELECT student_id, course_id, grade
FROM ranking
WHERE ranks = 1
GROUP BY student_id
ORDER BY student_id
