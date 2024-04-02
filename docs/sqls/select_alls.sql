-- + 조건 : 비 진성고객 리스트 필요(주문 1건 이하 포함)
SELECT Customers.CustomerID, Customers.CustomerName, COUNT(Orders.CustomerID)
FROM Customers
LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerID
HAVING COUNT(Orders.CustomerID) <= 1
;

-- Number of Records: 3
-- CustomerID	                    CustomerName	            COUNT(Orders.CustomerID)
-- 13	                        Centro comercial Moctezuma	                1
-- 22	                    FISSA Fabrica Inter. Salchichas S.A.	        0
-- 57	                            Paris spécialités	                    0


-- + 조건 : 판매자 중 수익 낮은 순위자 3명 정보, 총 판매액
SELECT Employees.EmployeeID, Employees.LastName, Employees.FirstName, sum(Products.Price*OrderDetails.Quantity) as TOTAL_PRICE
FROM Employees
LEFT JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID
LEFT JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID 
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY Employees.EmployeeID
ORDER BY TOTAL_PRICE ASC
limit 3 ;

-- EmployeeID	LastName	FirstName	TOTAL_PRICE
-- 5	Buchanan	Steven	129054.05
-- 9	Dodsworth	Anne	131552.75
-- 6	Suyama	Michael	181913.85

-- + 조건 : 배송 회사별 총 배송 건수와 총 제품 금액 정보
SELECT Shippers.ShipperID, Shippers.ShipperName, COUNT(Orders.OrderID) AS TOTAL_DELIVERY, SUM(Products.Price * OrderDetails.Quantity) AS TOTAL_PRICE
FROM Shippers
LEFT JOIN Orders
ON Shippers.ShipperID = Orders.ShipperID
LEFT JOIN OrderDetails
ON Orders.OrderID = OrderDetails.OrderID
LEFT JOIN Products
ON OrderDetails.ProductID = Products.ProductID
GROUP BY ShipperName
ORDER BY ShipperID ASC ;

-- Number of Records: 3
-- ShipperID	ShipperName	TOTAL_DELIVERY	TOTAL_PRICE
-- 1	Speedy Express	646	395931.17
-- 2	United Package	864	610889.89
-- 3	Federal Shipping	645	442546.25

-- + 조건 : 제품 회사별 총 판매액과 정보
SELECT Suppliers.SupplierID, Suppliers.SupplierName, SUM(Products.Price * OrderDetails.Quantity) AS TOTAL_PRICE
FROM Suppliers
LEFT JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
LEFT JOIN OrderDetails
ON Products.ProductID = OrderDetails.ProductID
GROUP BY Suppliers.SupplierName
ORDER BY Suppliers.SupplierID ASC ;

-- Number of Records: 29
-- SupplierID	SupplierName	TOTAL_PRICE
-- 1	Exotic Liquid	38267.00
-- 2	New Orleans Cajun Delights	36073.55
-- 3	Grandma Kelly's Homestead	45295.00
-- 4	Tokyo Traders	35187.00
-- 5	Cooperativa de Quesos 'Las Cabras'	27898.00
-- 6	Mayumi's	16630.00
-- 7	Pavlova, Ltd.	123827.10
-- 8	Specialty Biscuits, Ltd.	52152.10
-- 9	PB Knäckebröd AB	12528.00
-- 10	Refrescos Americanas LTDA	5062.50
-- 11	Heli Süßwaren GmbH & Co. KG	43991.69
-- 12	Plutzer Lebensmittelgroßmärkte AG	165370.59
-- 13	Nord-Ost-Fisch Handelsgesellschaft mbH	15844.68
-- 14	Formaggi Fortini s.r.l.	55015.30
-- 15	Norske Meierier	50317.00
-- 16	Bigfoot Breweries	25554.00
-- 17	Svensk Sjöföda AB	22940.00
-- 18	Aux joyeux ecclésiastiques	178434.50
-- 19	New England Seafood Cannery	29761.85
-- 20	Leka Trading	48127.45
-- 21	Lyngbysild	11402.00
-- 22	Zaanse Snoepfabriek	6367.00
-- 23	Karkki Oy	31876.75
-- 24	G'day, Mate	74139.60
-- 25	Ma Maison	27296.75
-- 26	Pasta Buttini s.r.l.	56457.00
-- 27	Escargots Nouveaux	7075.50
-- 28	Gai pâturage	135898.00
-- 29	Forêts d'érables	70577.40

-- + 조건 : 카테고리별 판매 합계 정보
SELECT Categories.CategoryID, Categories.CategoryName, SUM(Products.Price * OrderDetails.Quantity) AS TOTAL_PRICE
FROM Categories
LEFT JOIN Products
ON Categories.CategoryID = Products.CategoryID
LEFT JOIN OrderDetails
ON Products.ProductID = OrderDetails.ProductID 
GROUP BY CategoryID 
ORDER BY Categories.CategoryID ASC; 

-- Number of Records: 8
-- CategoryID	CategoryName	TOTAL_PRICE
-- 1	Beverages	309582.25
-- 2	Condiments	122343.00
-- 3	Confections	190328.54
-- 4	Dairy Products	269128.30
-- 5	Grains/Cereals	106848.00
-- 6	Meat/Poultry	190682.69
-- 7	Produce	111395.00
-- 8	Seafood	149059.53