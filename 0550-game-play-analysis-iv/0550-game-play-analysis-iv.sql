with first as (select player_id, min(event_date) as event_date
              from activity
              group by player_id)
select round(sum(datediff(a.event_date, f.event_date) = 1) / count(distinct a.player_id), 2) as fraction
from activity a
join first f on a.player_id = f.player_id