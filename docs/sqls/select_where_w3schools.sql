SELECT * 
FROM Customers
-- WHERE CustomerID = 80 -- COUNT : 12
-- WHERE CustomerID <> 80 -- COUNT : 90
-- WHERE CustomerID BETWEEN 20 AND 30 -- COUNT : 11
-- WHERE (CustomerID >= 20) AND (CustomerID <= 30); -- COUNT : 11
-- WHERE CustomerID IN (1, 3, 5, 10); -- COUNT : 4
-- WHERE City = 'London'; -- COUNT : 6
-- WHERE City IN ('London', 'Berlin'); -- COUNT : 7
--  WHERE City IN ('London', 'Berlin') AND CustomerID <= 11;