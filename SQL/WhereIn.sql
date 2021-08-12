SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = "Lucy" or NAME="Ella" or NAME="Pickle" or NAME="Rogan" or NAME="Sabrina"
or NAME="Mitty"
ORDER BY ANIMAL_ID

-- 작동이 잘 되지만 가독성을 위해 in을 활용할 수 있다 아래와 같음

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ("Lucy","Ella","Pickle","Rogan","Sabrina","Mitty")
ORDER BY ANIMAL_ID