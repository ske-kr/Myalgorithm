SELECT ID,NAME,HOST_ID
FROM PLACES
WHERE HOST_ID IN( SELECT HOST_ID
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING COUNT(HOST_ID)>1)

-- dev matching 헤비유저찾기 문제
-- sub query를 활용해서 HOST ID카운트후 2개이상인 것들에 대해 데이터를 출력하도록 했다.

-- 더 나은 답안, 이유는 EXISTS를 활용하게 되면 찾게 된 후 더이상 탐색x
-- IN의 경우에는 모든 대상에 대한 탐색이 끝까지 진행된다.

SELECT ID,NAME,HOST_ID
FROM PLACES
WHERE HOST_ID EXISTS( SELECT HOST_ID
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING COUNT(HOST_ID)>1)