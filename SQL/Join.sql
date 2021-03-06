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

SELECT INS.NAME,INS.DATETIME
FROM ANIMAL_INS INS
LEFT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY DATETIME LIMIT 3

-- left, right, inner join 모두 on id=id형태를 기억하도록 하자!
-- 여기서 처음보는 것은 LIMIT 3이라는 조건절이고 이는 정렬 후 상위 3개 값만 추출한다는 것이다.

SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS
JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID 
ORDER BY Date(OUTS.DATETIME)-DATE(INS.DATETIME) DESC LIMIT 2;

-- DATE는 날짜만 추출해준다.