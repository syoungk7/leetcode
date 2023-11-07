# Write your MySQL query statement below
# select p.product_name, s.year, s.price
# from Sales as s, Product as p
# where s.product_id = p.product_id

select p.product_name, s.year, s.price
from Sales as s
right join Product p on s.product_id = p.product_id
where s.price is not Null