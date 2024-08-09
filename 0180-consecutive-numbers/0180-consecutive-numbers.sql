# Write your MySQL query statement below

# select distinct num as ConsecutiveNums
# from (select id-1, num,
#         lag(num) over (order by id) as prev_num,
#         lead (num) over (order by id) as next_num from logs) as sub
# where num = prev_num and prev_num = next_num


# select *,
#     lag(num) over (order by id) as prev_num,
#     lead (num) over (order by id) as next_num 
# from logs
# where 

with CTE as (
    select
        num,
        id,
        lead(num, 1)  over (order by id) num1,
        lead(num, 2)  over (order by id) num2,
        lead(id, 1) over (order by id) id1,
        lead(id, 2) over (order by id) id2
    from logs
)

select distinct num as "ConsecutiveNums" from cte
where num = num1 and num = num2 and id = id1 - 1 and id = id2 -2;


# With test as (
#     select *, row_number() over(order by id) as row_num
#     from Logs)

# select distinct num as ConsecutiveNums
# from (select num,
#     lag(num) over (order by row_num) as prev_num,
#     lead(num) over (order by row_num) as next_num from test) as sub
# where num = prev_num and prev_num = next_num and 


# select num,
# lag(num) over (order by row_num) as prev_num,
# lead (num) over (order by row_num) as next_num 
# from test
