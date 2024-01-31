# Write your MySQL query statement below
WITH temp AS (SELECT fail_date AS test_date, 'failed'  AS period_state, 
                    ROW_NUMBER () OVER (ORDER BY fail_date) AS test_rm
                FROM Failed
                WHERE fail_date between '2019-01-01' AND '2019-12-31'
                UNION
                SELECT success_date AS test_date, 'succeeded' AS period_state, 
                    ROW_NUMBER () OVER (ORDER BY success_date) AS test_rm
                FROM Succeeded
                WHERE success_date between '2019-01-01' AND '2019-12-31')

SELECT period_state, MIN(test_date) AS start_date, MAX(test_date) AS end_date
FROM (SELECT *, ROW_NUMBER () OVER (ORDER BY test_date) AS total_rm
      FROM temp
      ORDER BY test_date) t
GROUP BY total_rm - test_rm, period_state
ORDER BY test_date


# DATEDIFF(fail_date, '2019-01-01')
# DATEDIFF(success_date, '2019-01-01')