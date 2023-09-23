/* Write your PL/SQL query statement below */
Select Product.product_name, Sales.year, Sales.price
From Sales
Inner Join Product On Sales.product_id = Product.product_id