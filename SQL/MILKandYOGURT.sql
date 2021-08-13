SELECT DISTINCT CART_ID
FROM CART_PRODUCTS 
WHERE NAME="Milk" and 
    CART_ID in (SELECT CART_ID
                FROM CART_PRODUCTS
                WHERE NAME="Yogurt"
    )
ORDER BY CART_ID;

-- 서브쿼리를 활용한 예시이다
-- yogurt를 가지고있는 데이터를 추출하고 해당데이터에 있는 id가 있는 milk 소유자를 뽑아냇다
-- 여기서 DISTINCT는 중복값 제거의 목적이라고 보면 된다.

SELECT DISTINCT A.CART_ID
FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') A
JOIN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') B
ON A.CART_ID = B.CART_ID

-- join을 활용한 것이고(inner join) 사실은 조금 더 직관적이기에 이 방법을 사용하길 추천한다
-- 일반적인 inner join처럼 ID가 양쪽에 존재하는 data를 뽑아낸 것이다.
