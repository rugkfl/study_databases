-- - 다음 조건은 subquery 사용
-- - Table : Customers, Orders
-- + 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기
SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (SELECT CustomerID  
					FROM Orders
					GROUP BY CustomerID
					HAVING COUNT(CustomerID) >= 5) 
;

-- Number of Records: 72 

-- - Table : Orders
-- 주문 건수 20개 이상을 받은 판매자 정보
SELECT EmployeeID, Notes
FROM Employees
WHERE EmployeeID IN (SELECT EmployeeID 
					FROM Orders
					GROUP BY EmployeeID
					HAVING COUNT(EmployeeID) >= 20
                    ORDER BY EmployeeID ASC)
;
-- Number of Records: 9

-- - Table : Suppliers
-- + 조건 : CategoryID를 가장 많이 제공 상위 2개 회사 정보
SELECT * 
FROM Suppliers
WHERE SupplierID IN (SELECT SupplierID
						FROM Products
						GROUP BY CategoryID
						HAVING COUNT(CategoryID) >= 12 
						)
;
-- Number of Records: 3

--  SELECT SupplierID, COUNT(SupplierID),CategoryID  
--     FROM Products
--     GROUP BY CategoryID
--     ORDER BY COUNT(SupplierID) DESC
--     LIMIT 2;
