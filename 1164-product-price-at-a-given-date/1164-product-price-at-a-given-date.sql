# Write your MySQL query statement below
SELECT p.product_id, IF(s.max_date is null, 10, new_price) AS price
FROM Products p

LEFT JOIN (
    SELECT product_id, MAX(change_date) as max_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
    ) s 
    ON p.product_id = s.product_id

WHERE p.change_date = s.max_date or s.max_date is null
GROUP BY p.product_id

# SELECT *, (rank() OVER price_rank) AS price_rank
# FROM Products p
# WINDOW price_rank AS (PARTITION BY product_id ORDER BY change_date DESC)

# LEFT JOIN (
    # SELECT product_id, new_price, change_date, (rank() OVER price_rank) AS price_rank
    # FROM Products
    # WHERE change_date <= '2019-08-16'
    # WINDOW price_rank AS (PARTITION BY product_id ORDER BY change_date DESC)) s
    # ON p.product_id = s.product_id

    # SELECT product_id, change_date
    #        FROM Products
    #        #WHERE change_date <= '2019-08-16'
    #        GROUP BY product_id 
    #        HAVING MAX(change_date) >= change_date 