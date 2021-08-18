SELECT ANIMAL_ID,NAME, CASE
                        WHEN SEX_UPON_INTAKE LIKE "%Spayed%" THEN "O"
                        WHEN SEX_UPON_INTAKE LIKE "%Neutered%" THEN "O"
                        ELSE "X"
                        END as "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- case절 활용예시
-- case는 SELECT에서 활용한다.