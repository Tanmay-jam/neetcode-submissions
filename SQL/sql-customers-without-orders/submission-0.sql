-- Write your query below
SELECT DISTINCT name FROM customers
WHERE name NOT IN (
    SELECT name 
    FROM orders
    JOIN customers
    ON orders.customer_id=customers.id
);