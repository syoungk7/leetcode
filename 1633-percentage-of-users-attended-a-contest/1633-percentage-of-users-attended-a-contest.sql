SELECT r.contest_id,
       ROUND(count(distinct r.user_id)/count(distinct u.user_id)* 100,2) as percentage
FROM Register r, Users u
GROUP BY r.contest_id
ORDER BY percentage desc, r.contest_id asc;
