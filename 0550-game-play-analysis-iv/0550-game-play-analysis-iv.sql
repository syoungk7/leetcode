with first_login as (
    select player_id, min(event_date) as first_login_date
    from activity
    group by player_id)

select round(count(distinct f.player_id) * 1.0 / (select count(distinct player_id) from Activity), 2) as fraction
from first_login f
join activity a on f.player_id = a.player_id
and a.event_date = date_add(f.first_login_date, interval 1 day)