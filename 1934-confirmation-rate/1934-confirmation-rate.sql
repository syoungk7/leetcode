# Write your MySQL query statement below
select s.user_id, round(ifnull(c.confirmed/(c.timeout+c.confirmed), 0), 2) as confirmation_rate
from signups as s
left join (select user_id, count(case when action = 'timeout' then 1 end) as timeout,
        count(case when action = 'confirmed' then 1 end) as confirmed
        from confirmations
        group by user_id) as c
on s.user_id = c.user_id