-- - Table : Products
-- + 조건 : CategoryID 가 10개 이상

SELECT COUNT(CategoryID) AS CNT ,CategoryID  
FROM Products
GROUP BY CategoryID
HAVING COUNT(CategoryID) >= 10 ;
 -- Number of Records: 5

--- Table : Customers, Orders
-- - 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기
SELECT COUNT(CustomerID) AS CNT, CustomerID  
FROM Orders
GROUP BY CustomerID
HAVING COUNT(CustomerID) >= 5;

SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (20, 37, 41, 46, 51, 63, 65, 75, 87)
;
-- Number of Records: 9

-- - Table : Orders
-- - 조건 : 주문 갯수가 20개 이상인 회사 LastName과 갯수

SELECT COUNT(EmployeeID) AS CNT, EmployeeID 
FROM Orders
GROUP BY EmployeeID
HAVING COUNT(EmployeeID) >= 20;

SELECT EmployeeID, LastName
FROM Employees
WHERE EmployeeID IN (1, 2, 3, 4, 8);
-- Number of Records: 5


