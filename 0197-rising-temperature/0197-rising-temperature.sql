/* Write your PL/SQL query statement below */
With tmp_weather (id, recordDate, temperature, prev_day, prev_tem)
As (Select id, recordDate, temperature,
    Lag(recordDate) over (Order by recordDate) prev_day,
    Lag(temperature) over (Order by recordDate) prev_tem
    From Weather
    )
Select id
From tmp_weather
Where temperature - prev_tem > 0 and 
    trunc(recordDate) - trunc(prev_day) = 1