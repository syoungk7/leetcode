# Write your MySQL query statement below

# with noc as (
# select user_id, count(action) as num_of_confirmed
# from Confirmations
# where action = 'confirmed'
# group by user_id, action
# )
# # {"headers": ["user_id", "num_of_confirmed"], "values": [[7, 3], [2, 1]]}

# select s.user_id, ifnull(n.num_of_confirmed/count(c.user_id), 0) as confirmation_rate
# from Signups s
# left join Confirmations c on s.user_id = c.user_id
# left join noc n on c.user_id = n.user_id
# group by c.user_id
# # {"headers": ["user_id", "num_of_action"], "values": [[3, 2], [7, 3], [2, 2], [6, 0]]}

# select s.user_id, round(avg(if(c.action="confirmed", 1, 0)), 2) as confirmation_rate
# from Signups s 
# left join Confirmations c on s.user_id = c.user_id 
# group by user_id



# Select s.user_id, case when c.action is NULL then 0.00 else Round((sum(c.action = 'confirmed')/count(c.action)),2 )end as confirmation_rate
# From Signups s
# left join
# Confirmations c
# on s.user_id = c.user_id
# group by s.user_id;



Select s.user_id, ifnull(round(sum(case when c.action='confirmed' then 1 else 0 end)/count(c.user_id), 2), 0) as confirmation_rate
From Signups s
left join Confirmations c on s.user_id = c.user_id
group by s.user_id;