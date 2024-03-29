SELECT COUNT(Country), Country
FROM Customers
GROUP BY Country;

SELECT COUNT(Country) AS CNT, Country, MAX(PostalCode) AS MAX_POST
FROM Customers
GROUP BY Country;

-- GROUP BY 쓰지 않은 컬럼명을 SELECT에 넣을 경우 합쳐진 값이 아닌 첫번 째의 값만 나옴

-- GROUP BY를 쓰면 집계함수
-- HAVING은 GROUP BY의 조건절