# Write your MySQL query statement below
# WITH Scores AS (SELECT t.first_player, p.player_id, SUM(t.first_score) AS total_scores, p.group_id
#                 FROM (SELECT first_player, first_score
#                       FROM Matches
#                       UNION 
#                       SELECT second_player AS first_player, second_score AS first_score
#                       FROM Matches) t, Players p
#                 WHERE p.player_id = t.first_player
#                 GROUP BY player_id
#                 ORDER BY p.group_id, total_scores DESC, player_id)

# SELECT group_id, player_id
# FROM Scores
# GROUP BY group_id


# # Write your MySQL query statement below
# WITH Scores AS (SELECT t.player, SUM(t.score) AS total_scores
#                 FROM (SELECT first_player AS player, first_score AS score
#                       FROM Matches
#                       UNION 
#                       SELECT second_player AS player, second_score AS score
#                       FROM Matches) t
#                 GROUP BY t.player)

# SELECT DISTINCT p.group_id, FIRST_VALUE(p.player_id) OVER tmp AS player_id
# FROM Players p
# LEFT JOIN Scores s ON p.player_id = s.player
# WINDOW tmp AS (PARTITION BY p.group_id ORDER BY s.total_scores DESC, p.player_id ASC)

select group_id, player_id from (
	select p.group_id, ps.player_id, sum(ps.score) as score from Players p,
	    (select first_player as player_id, first_score as score from Matches
	    union all
	    select second_player, second_score from Matches) ps
	where p.player_id = ps.player_id
	group by ps.player_id order by group_id, score desc, player_id) top_scores
group by group_id