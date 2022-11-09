https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

Find all customers in Berlin

SELECT * FROM Customers
where city = 'Berlin';

Find all customers in Mexico City

SELECT * FROM Customers
WHERE city = 'México D.F.';

Find avg price of all products

SELECT avg(price) as average_price FROM products;

Find number of products that Have price = 18

SELECT count(*) as num_products FROM products
WHERE price = 18;


Find orders between 1996-08-01 and 1996-09-06

SELECT * FROM Orders
WHERE orderDate BETWEEN '1996-08-01' AND '1996-09-60'

Find customers with more than 3 orders

SELECT *, count(Orders.CustomerID) as orders FROM Customers
JOIN Orders
GROUP BY Orders.CustomerID
HAVING count(Orders.CustomerID) > 3

Find all customers that are from the same city (Not quite sure what you want with this query)

SELECT *
FROM Customers
GROUP BY city