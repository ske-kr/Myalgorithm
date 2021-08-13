SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%el%" AND ANIMAL_TYPE = "Dog"
ORDER BY NAME

-- like활용 예제, 여기서 %는 regex에서 임의문자*와 같다.(blank도 탐색해냄)
-- 추가로 and,or,not,in 등의 예시를 WHERE에서 활용가능하다.