# Write your MySQL query statement below
select s.student_id, s.student_name, s.subject_name, count(e.student_id) as attended_exams
from (select student_id, student_name, subject_name
      from Students, Subjects) s
left outer join Examinations e on e.student_id = s.student_id and e.subject_name = s.subject_name
group by s.student_id, s.subject_name
order by s.student_id, s.subject_name