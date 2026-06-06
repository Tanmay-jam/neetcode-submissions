-- Write your query below
SELECT EMPLOYEE_ID, 
    CASE
        WHEN employee_id%2=1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END as bonus
FROM employees
ORDER BY employee_id;
