# Write your MySQL query statement below

# WITH temp AS (SELECT e1.employee_id,
#                 sum(1) over (ORDER BY e3.manager_id) as c_sum
#               FROM Employees e1
#               LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id
#               LEFT JOIN Employees e3 ON e2.manager_id = e3.employee_id
#               WHERE e3.manager_id = 1 AND e1.employee_id != e1.manager_id)
# SELECT employee_id
# FROM temp
# WHERE c_sum >= 3

## ref: https://dev.mysql.com/blog-archive/mysql-8-0-labs-recursive-common-table-expressions-in-mysql-ctes-part-three-hierarchies/

WITH RECURSIVE tmp AS
    (SELECT employee_id, employee_name, manager_id, 1 AS depth
     FROM Employees 
     WHERE employee_id != 1 AND manager_id = 1
     UNION ALL
     SELECT e.employee_id, e.employee_name, tmp.manager_id, tmp.depth+1 
     FROM Employees e, tmp
     WHERE tmp.employee_id = e.manager_id)

SELECT DISTINCT employee_id
FROM tmp
WHERE (SELECT COUNT(employee_id)
       FROM tmp
       WHERE depth = 1 OR depth = 2) >= 3

# SELECT DISTINCT employee_id
# FROM tmp t, (SELECT manager_id, depth, 
#                 sum(depth) over (PARTITION BY manager_id, depth) as cumulative_sum
#              FROM tmp) tt
# WHERE tt.depth >= 2 AND cumulative_sum >= 3 AND t.manager_id = tt.manager_id AND t.employee_id != tt.manager_id





# WITH RECURSIVE tmp AS
#     (SELECT employee_id, employee_name, manager_id, 0 AS depth 
#      FROM Employees 
#      WHERE manager_id = employee_id
#      UNION ALL
#      SELECT e.employee_id, e.employee_name, tmp.manager_id, tmp.depth+1 
#      FROM Employees e, tmp
#      WHERE tmp.employee_id = e.manager_id AND e.employee_id != e.manager_id)

# SELECT DISTINCT employee_id
# FROM tmp t, (SELECT manager_id, depth, 
#                 sum(depth) over (PARTITION BY manager_id, depth) as cumulative_sum
#              FROM tmp) tt
# WHERE tt.depth >= 2 AND cumulative_sum >= 3 AND t.manager_id = tt.manager_id AND t.employee_id != tt.manager_id