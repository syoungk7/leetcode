WITH T as (SELECT query_name,
    AVG(rating/position) as q,
    SUM(if(rating <3, 1,0)) as p,
    count(*) as total
FROM Queries
WHERE query_name is NOT NULL
GROUP BY query_name)

SELECT query_name,
      ROUND(q,2) as quality,
      ROUND((p/total *100),2) as poor_query_percentage
FROM T;
