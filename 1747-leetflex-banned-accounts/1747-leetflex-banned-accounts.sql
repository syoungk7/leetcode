# Write your MySQL query statement below
SELECT DISTINCT(a.account_id)
FROM LogInfo a, LogInfo b
WHERE a.account_id = b.account_id AND a.ip_address != b.ip_address AND
    (a.login BETWEEN b.login AND b.logout OR a.logout BETWEEN b.login AND b.logout)