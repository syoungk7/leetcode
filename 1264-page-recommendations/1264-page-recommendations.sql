# Write your MySQL query statement below
WITH friends AS (SELECT user2_id AS id
                 FROM Friendship
                 WHERE user1_id < user2_id AND user1_id = 1
                 UNION
                 SELECT user1_id  AS id
                 FROM Friendship
                 WHERE user1_id > user2_id AND user2_id = 1)

SELECT DISTINCT(page_id) AS recommended_page
FROM Likes
WHERE user_id IN (SELECT * FROM friends) AND 
    page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)