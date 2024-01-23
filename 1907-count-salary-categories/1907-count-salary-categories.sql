# Write your MySQL query statement below
# WITH selected AS (
#                 SELECT s.category, COUNT(s.category) AS accounts_count
#                 FROM (
#                     SELECT account_id,
#                         CASE 
#                             WHEN income < 20000 THEN 'Low Salary'
#                             WHEN income <= 50000 THEN 'Average Salary'
#                             ELSE 'High Salary'
#                         END AS category
#                     FROM Accounts
#                     ) s
#                 GROUP BY s.category
#                 )

# SELECT n.category, IFNULL(s.accounts_count, 0) AS accounts_count
# FROM selected s
# RIGHT JOIN (
#             SELECT 'Low Salary' as category
#             UNION
#             SELECT 'Average Salary' as category
#             UNION
#             SELECT 'High Salary' as category
#             ) n ON n.category = s.category


# SELECT 'Low Salary' AS category,
#   SUM(CASE WHEN income < 20000 THEN 1 ELSE 0 END) AS accounts_count
# FROM Accounts
# UNION
# SELECT 'Average Salary' category,
#   SUM(CASE WHEN income >= 20000 AND income <= 50000 THEN 1 ELSE 0 END) AS accounts_count
# FROM Accounts
# UNION
# SELECT 'High Salary' category,
#   SUM(CASE WHEN income > 50000 THEN 1 ELSE 0 END) AS accounts_count
# FROM  Accounts

SELECT "Low Salary" AS category,
       sum(income < 20000) AS accounts_count
  FROM Accounts

UNION

SELECT "Average Salary" AS category,
       sum(income BETWEEN 20000 AND 50000) AS accounts_count
  FROM Accounts

UNION

SELECT "High Salary" AS category,
       sum(income > 50000) AS accounts_count
  FROM Accounts;