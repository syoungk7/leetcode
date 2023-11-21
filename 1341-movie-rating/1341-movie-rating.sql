# Write your MySQL query statement below

SELECT s.results
FROM ((SELECT u.name AS results, COUNT(m.movie_id) AS highest_count
       FROM MovieRating m, Users u
       WHERE m.user_id = u.user_id
       GROUP BY m.user_id
       ORDER BY highest_count DESC, u.name
       LIMIT 1)
      UNION
      (SELECT v.title AS results, AVG(m.rating) AS highest_avg
       FROM MovieRating m, Movies v
       WHERE m.created_at between '2020-02-01' and  '2020-02-29' and m.movie_id = v.movie_id
       GROUP BY m.movie_id
       ORDER BY highest_avg DESC, v.title
       LIMIT 1)) s
