with productsales as (
  select p.product_id,
        case when u.units is null then 0 else u.units end as units, 
        p.price,
        case when u.units is null then 0 else u.units * p.price end as total_price
  from prices p
  left join UnitsSold u on u.product_id = p.product_id
  and u.purchase_date between p.start_date and p.end_date)

select product_id,
  case when sum(units) = 0 then 0
  else round(sum(total_price) / sum(units), 2)
  end as average_price
from productsales
group by product_id