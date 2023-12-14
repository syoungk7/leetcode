# Write your MySQL query statement below
# WITH ranking AS (
#     SELECT student_id, course_id, grade,
#         RANK() OVER (PARTITION BY student_id ORDER BY grade DESC) AS ranks
#     FROM Enrollments
#     ORDER BY student_id, course_id)

# SELECT student_id, course_id, grade
# FROM ranking
# WHERE ranks = 1
# GROUP BY student_id
# ORDER BY student_id

WITH ranking AS (
    SELECT student_id, course_id, grade,
        RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id) AS ranks
    FROM Enrollments
    ORDER BY student_id, course_id)

SELECT student_id, course_id, grade
FROM ranking
WHERE ranks = 1
# GROUP BY student_id
# ORDER BY student_id

# with t as(
#     select *,
#     dense_rank() over(partition by student_id order by grade desc) rnk
#     from Enrollments
#     order by course_id
# )
# select student_id, course_id, grade
# from t
# where rnk =1 
# group by student_id
# having min(course_id)
# order by student_id