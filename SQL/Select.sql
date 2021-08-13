SELECT NAME,DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

-- 단순 select, 여기서 DESC를 ORDER BY에 넣어주면 역순으로 정렬할 수 있다.

SELECT Min(DATETIME) as '시간'
FROM ANIMAL_INS

-- Min, Max 등을 select조건절에 활용할 수 있다. 그외 count, sum 등이 있다