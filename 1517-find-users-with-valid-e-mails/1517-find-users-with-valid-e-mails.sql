# Write your MySQL query statement below
Select *
from users
where REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$')

## '^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\\.com$'