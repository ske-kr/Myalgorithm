SELECT NAME,DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

-- 단순 select, 여기서 DESC를 ORDER BY에 넣어주면 역순으로 정렬할 수 있다.

SELECT Min(DATETIME) as '시간'
FROM ANIMAL_INS

-- Min, Max 등을 select조건절에 활용할 수 있다. 그외 count, sum 등이 있다

SELECT HOUR(DATETIME) as HOUR,COUNT(*) as COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME)>=9 and HOUR(DATETIME) < 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)

-- 알고보니 HOUR같은것도 있었다.. SET 명령어를 활용한 변수를 이용한 그룹화는 아래예시와 같이 활용가능하다

SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION !="Aged"
ORDER BY ANIMAL_ID;

-- != 와 <>의 차이점이 뭘까 - 동일하다고 한다 . 다만 <>이 dbms공통적으로 다쓰기때문에 <>를 쓰자 정도?
