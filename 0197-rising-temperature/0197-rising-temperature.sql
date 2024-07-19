# Write your MySQL query statement below
With tmp_weather (id, recordDate, temperature, prev_day, prev_tem)
As (Select id, recordDate, temperature,
    Lag(recordDate) over (Order by recordDate) prev_day,
    Lag(temperature) over (Order by recordDate) prev_tem
    From Weather
    )
  
Select id
From tmp_weather
Where temperature - prev_tem > 0 and TIMESTAMPDIFF(Day, prev_day, recordDate) = 1