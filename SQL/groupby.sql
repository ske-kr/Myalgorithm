SELECT BRANCH_ID, SUM(SALARY) as TOTAL
FROM EMPLOYEES
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID

-- GROUPBY 예제, 그룹화 후 그룹내 연봉의 sum까지 출력시키는 예시문제였다.



SELECT ANIMAL_TYPE, COUNT(*) as count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE;

-- 또다른 GROUPBY 예제, 그룹화 후 data count 활용문제