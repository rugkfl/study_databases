SELECT COUNT(Country) AS CNT, Country
FROM Customers
GROUP BY Country
HAVING COUNT(Country) >= 5;

