SELECT contest_id, ROUND(my.participants / u.usernum *100, 2) AS percentage
FROM  (SELECT contest_id, COUNT(user_id) AS participants
        FROM Register
        GROUP BY contest_id) my,
      (SELECT COUNT(user_id) AS usernum
        FROM Users) u
ORDER BY percentage DESC, contest_id ASC