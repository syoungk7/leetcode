# Write your MySQL query statement below

## 예전
# With tmp_weather (id, recordDate, temperature, prev_day, prev_tem)
# As (Select id, recordDate, temperature,
#     Lag(recordDate) over (Order by recordDate) prev_day,
#     Lag(temperature) over (Order by recordDate) prev_tem
#     From Weather
#     )
# Select id
# From tmp_weather
# Where temperature - prev_tem > 0 and TIMESTAMPDIFF(Day, prev_day, recordDate) = 1

# join
select w.id
from Weather w
Join Weather e on TIMESTAMPDIFF(Day, e.recordDate, w.recordDate) = 1 and w.temperature - e.temperature > 0

# where
# select w.id
# from Weather w, Weather e
# where TIMESTAMPDIFF(Day, w.recordDate, e.recordDate) = 1 and w.temperature - e.temperature > 0