# Write your MySQL query statement below
SELECT ad_id, 
    IFNULL(ROUND(SUM(IF(action = 'Clicked', 1, 0 )) / SUM(IF(action != 'Ignored', 1, 0)) * 100, 2), 0) as ctr
FROM ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id