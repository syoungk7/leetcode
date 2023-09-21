/* Write your PL/SQL query statement below */

/* Select user_id, INITCAP(lower(name)) as name */
Select user_id, concat(upper(SUBSTR(name, 1, 1)), lower(SUBSTR(name, 2, length(name)))) as name
From users
Order by user_id