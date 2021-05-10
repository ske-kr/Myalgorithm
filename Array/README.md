greedy part, 기본 입출력 format 및 mapping 습관들이기



중요 !
## list reference 관련 문제
a = b
둘다 리스트 일시 복사가 아닌 *a=&b가 되어서 (즉 참조가 되어서 )

한곳을 변경하면 나머지 한곳도 변경됌

3가지 방법 존재

1. 한 원소씩 append 혹은 한 원소씩 복사
2. copy()사용 => a=b.copy()
3. slicing  => a=b[:]


## sort by key
list sort의 key값 설정하기

주로 2d list에 활용된다.

list data의 크기로 정렬이 아닌

len()함수를 이용한다던지, list[0] list[1]값의 차이를 이용한다던지
list[1]의 값을 통해 정렬한다던지..

예시 . a=[[1,2],[1,3],[1,1]]
a.sort(key=lambda x : x[1])
a는 [[1,1],[1,2],[1,3]]으로 정렬된다


## set method

set은 중복을 고려하지 않고 순서가 없이 데이터를 정렬
[1,1,1,2,2,2,3,3,3]을 set시키면
set(a)={1,2,3}이 된다..

이러한 set은 교집합 차집합 등을 구하는데 압도적으로 유리하다.
교집합 a & b
합집합 a | b
차집합 a - b

## dictionary

if dic.get(a) is None:
a가 dic에 없다면


## slicing

슬라이싱은 아주 강력한 툴이다

[start:end:step]

start:시작지점
end : 도착지점
step : 어떤방식으로 읽을지(default=1)
step이 -1이라면 거꾸로 읽는다
예를들어
a[::-1]의 경우엔 리스트를 뒤집게 만드는 것이고
reverse()메소드와 동일한 역할을 할것이다.