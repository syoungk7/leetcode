# Write your MySQL query statement below
SELECT e.left_operand, e.operator, e.right_operand, 
    CASE e.operator
		WHEN '>' THEN IF(v.value > a.value, 'true', 'false')
        WHEN '<' THEN IF(v.value < a.value, 'true', 'false')
        WHEN '=' THEN IF(v.value = a.value, 'true', 'false')
        ELSE False
	end value
FROM Expressions e
JOIN Variables v ON (e.left_operand = v.name)
JOIN Variables a ON (e.right_operand = a.name)