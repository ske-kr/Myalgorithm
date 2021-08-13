
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL;


-- 주로 NULL값인 경우를 쉽게 찾아내는 케이스, 당연히 is not null도 가능하다.
-- NVL을 활용하거나 IFNULL을 활용하는 예시도 알아둬야함
-- IFNULL 예시

SELECT ANIMAL_TYPE, IFNULL(NAME,"No name") as NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS