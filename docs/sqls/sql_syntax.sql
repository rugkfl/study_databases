SELECT column_name(s) -- 컬럼 명
FROM table_name  -- 테이블 이름
WHERE condition -- FROM의 조건문
GROUP BY column_name(s) -- 집계함수를 통해 그룹화
HAVING condition -- GRUOP BY의 조건문
ORDER BY column_name(s); --  정렬화