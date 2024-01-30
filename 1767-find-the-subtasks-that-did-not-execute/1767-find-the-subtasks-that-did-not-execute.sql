# Write your MySQL query statement below

## https://dev.mysql.com/doc/refman/8.0/en/with.html#common-table-expressions-recursive
# WITH RECURSIVE cte (n) AS
# (
#   SELECT 1
#   UNION ALL
#   SELECT n + 1 FROM cte WHERE n < 5
# )
# SELECT * FROM cte;

WITH RECURSIVE cte AS (SELECT task_id, subtasks_count, 1 AS subtask_id
                       FROM Tasks
                       UNION ALL
                       SELECT task_id, subtasks_count, subtask_id + 1
                       FROM cte
                       WHERE subtask_id < subtasks_count)

SELECT task_id, subtask_id
FROM cte
WHERE (task_id, subtask_id) NOT IN (SELECT task_id, subtask_id FROM Executed)