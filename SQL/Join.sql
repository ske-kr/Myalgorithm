SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_OUTS a 
LEFT JOIN ANIMAL_INS b
ON a.ANIMAL_ID=b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL
ORDER BY a.ANIMAL_ID;

-- LEFT JOIN과 LEFT OUTER JOIN은 같은 명령어다
-- ON 은 JOIN문의 조건절이라고 이해하면 쉬울 것 같다.

SELECT INS.ANIMAL_ID as ANIMAL_ID, INS.NAME as NAME
FROM ANIMAL_INS as INS
JOIN ANIMAL_OUTS as OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME

-- 있었는데요 없었습니다 문제
-- 마찬가지로 ON의 활용문제이고, 해당문제는 공통부분만 출력하면 되므로 JOIN을 활용했다.