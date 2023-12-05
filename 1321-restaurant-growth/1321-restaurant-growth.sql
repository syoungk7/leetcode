# Write your MySQL query statement below

## 월 바뀐거에는 계산 안됨
SELECT s.visited_on, s.amount, s.average_amount
FROM (
    SELECT visited_on, 
        SUM(SUM(amount)) 
            OVER (ORDER BY visited_on 
                  rows BETWEEN 6 preceding AND CURRENT ROW) AS amount,
        ROUND(AVG(SUM(amount)) 
            OVER (ORDER BY visited_on 
                  rows BETWEEN 6 preceding AND CURRENT ROW), 2) AS average_amount
    FROM Customer
    GROUP BY visited_on
    ) s
JOIN (
#     SELECT DISTINCT visited_on
#     FROM Customer
#     WHERE visited_on -6 IN (SELECT DISTINCT visited_on FROM Customer)
#     ORDER BY visited_on
    SELECT c.visited_on
    FROM Customer c, Customer u
    WHERE DATEDIFF(c.visited_on, u.visited_on) = 6
    GROUP BY visited_on
    ) c ON c.visited_on = s.visited_on
ORDER BY visited_on

# SELECT visited_on, 
#     SUM(SUM(amount)) 
#         OVER (ORDER BY visited_on 
#               rows BETWEEN 6 preceding AND CURRENT ROW) AS amount,
#     ROUND(AVG(SUM(amount)) 
#         OVER (ORDER BY visited_on 
#               rows BETWEEN 6 preceding AND CURRENT ROW), 2) AS average_amount
# FROM Customer
# GROUP BY visited_on
# ORDER BY visited_on
# LIMIT 6, 4


# SELECT c.visited_on
# FROM Customer c, Customer u
# WHERE DATEDIFF(c.visited_on, u.visited_on) = 6
# GROUP BY visited_on

