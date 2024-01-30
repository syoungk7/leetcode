# Write your MySQL query statement below
WITH temp AS (SELECT DISTINCT student_id
              FROM Exam e, (SELECT exam_id, MIN(score) AS min_s, MAX(score) AS max_s
                            FROM Exam
                            GROUP BY exam_id) t
              WHERE e.exam_id = t.exam_id AND (e.score = min_s OR e.score = max_s))

SELECT student_id, student_name
FROM Student
WHERE student_id IN (SELECT DISTINCT student_id FROM Exam) AND
    student_id NOT IN (SELECT student_id FROM temp)