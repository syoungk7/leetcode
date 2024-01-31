# Write your MySQL query statement below

# SELECT ee1.employee_id
# FROM Employees ee1
# CROSS JOIN Employees ee2
# WHERE ee1.employee_id = ee2.manager_id OR (ee1.employee_id != ee1.manager_id 
#     AND ee1.manager_id IN (SELECT e3.manager_id
#                            FROM Employees e1
#                            CROSS JOIN Employees e2
#                            CROSS JOIN Employees e3
#                            WHERE e1.manager_id = e2.employee_id AND 
#                                e2.manager_id = e3.employee_id AND 
#                                e2.manager_id  != e3.manager_id))

# SELECT e1.employee_id, e1.manager_id, e2.employee_id, e2.manager_id, e3.employee_id, e3.manager_id
# FROM Employees e1
# LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id
# LEFT JOIN Employees e3 ON e2.manager_id = e3.employee_id
# ORDER BY e1.employee_id

# WITH RECURSIVE cte AS
#     (SELECT category_id, name, 0 AS depth FROM category WHERE parent IS NULL
#       UNION ALL
#       SELECT c.category_id, c.name, cte.depth+1 FROM category c JOIN cte ON
#         cte.category_id=c.parent)
# SELECT * FROM cte ORDER BY depth;

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

# SELECT e.employee_id, e.employee_name, e.manager_id, tmp.depth+1 
# FROM Employees e, tmp
# WHERE tmp.employee_id = e.manager_id AND e.employee_id != e.manager_id 



# Write your MySQL query statement below
SELECT a.employee_id as EMPLOYEE_ID FROM Employees as a # those whose boss is 1
WHERE a.employee_id!=1 AND a.manager_id=1
UNION
SELECT b.employee_id FROM Employees as b #those whose boss' boss is 1
WHERE b.manager_id IN
(
    SELECT a.employee_id FROM Employees as a
    WHERE a.employee_id!=1 AND a.manager_id=1    
)
UNION
SELECT c.employee_id FROM Employees as c #those whose boss' boss' boss is 1
WHERE c.manager_id IN
(
    SELECT b.employee_id FROM Employees as b
    WHERE b.manager_id IN
    (
        SELECT a.employee_id FROM Employees as a
        WHERE a.employee_id!=1 AND a.manager_id=1    
    )
)
ORDER BY EMPLOYEE_ID;