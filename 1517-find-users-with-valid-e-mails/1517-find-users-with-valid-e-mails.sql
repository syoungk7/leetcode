/* Write your PL/SQL query statement below */

Select *
from users
where REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$')