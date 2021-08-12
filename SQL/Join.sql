SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_OUTS a 
LEFT JOIN ANIMAL_INS b
ON a.ANIMAL_ID=b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL
ORDER BY a.ANIMAL_ID;

-- LEFT JOIN과 LEFT OUTER JOIN은 같은 명령어다
-- ON 은 JOIN문의 조건절이라고 이해하면 쉬울 것 같다.