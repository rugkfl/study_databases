

SELECT * 
FROM Customers
WHERE Country NOT IN  ('Germany','USA');


-- - 조건 Country 가 Germany 와 USA가 아닌 것들
-- COUNT : 67

SELECT * 
FROM Customers
WHERE CustomerID BETWEEN 50 AND 89
AND City = 'London';

-- - 조건 : CustomerID가 50에서 89이고, City가 Berlin인 고객
-- COUNT : 2