# Myalgorithm

자주하는 실수 - 백준

import sys
input = sys.stdin.readline
선언 및 항상 함수형식으로 code를 짤것(속도에서 엄청난 차이가 남)

아주 강력한 툴인 append와 pop은 아주 유용하고 편하지만 필요하지 않은 경우에도 사용하게 될때는 주의하자

꼭 써야한다면 특히 del 을 자주 사용해야 하는경우라면

좀 더 적합한 자료구조는 없는지, 수행시간의 관점에서 더 나은 방법은 없는지를 고민해보자

+
기본 입출력 format 및 mapping 습관들이기

# Python 

https://wikidocs.net/16050
24 - 문서화
25 - shebang
27 - 함수의 인자
28 - 파이썬의 타입시스템
29 - 변수 scope (특히 4번)
31 - exception
38&39 - iterator, generator

집중도 있게 봐야할 것들

## queue
from collections import deque

d=deque() 형식으로 선언한다

method에는 크게 4가지

d.append()
d.appendleft()
d.pop()
d.popleft()

queue형식으로 사용할때는 deque구조가 훨씬 유리하므로
deque를 사용하고

stack은 list를 사용해도 된다(별차이안남 오히려 list가 좀더빠름).

## heapq
import heapq


heapq를 쓰는방식은

list선언후

heapq함수를 통해 집어넣는것이다

기본적으로 heapq는 min heap구조
a=[]

heapq.heappush(a,data)
여기서 data는 tuple형태도 가능하다
(예를 들어 Max힙을 구현하기위해 -data,data를 집어넣을수도 있다는 뜻이다)

heap의 이상적 사용
heap은 내부적으로 가장 작은 값이 0 index에 존재하는 트리구조고
여기서 위의 괄호 예시처럼 -값을 tuple로 넣어준 이유는
max heap을 만들어주기 위해서 그렇다.(즉 0 index에 최대값이 존재하게 하려고)

# DFS & BFS

dfs 와 bfs의 차이점을 인지해야한다.
간단하게나마 구현방식에서의 차이점이라고 하면
bfs는 queue를 주로 활용, dfs는 recursive하게 활용한다는 점을 기억하면 좋을것이다.

※ 깊이 우선 탐색(DFS)의 시간 복잡도
- DFS는 그래프(정점의 수 : N, 간선의 수: E)의 모든 간선을 조회함
* 인접 리스트로 표현된 그래프 : O(N+E)
* 인접 행렬로 표현된 그래프 : O(N^2)

BFS와도 동일

- 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS) 활용한 문제 유형/응용

DFS, BFS은 특징에 따라 사용에 더 적합한 문제 유형들이 존재한다.

1) 그래프의 모든 정점을 방문하는 것이 주요한 문제
 - 둘 중 편한 것을 사용하시면 된다.

2) 경로의 특징을 저장해둬야 하는 문제
 - 예를 들면 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제 등, 각각의 경로마다 특징을 저장해둬야 할 때는 DFS를 사용. (BFS는 경로의 특징을 가지지 못하므로)

3) 최단거리 구해야 하는 문제
 - 미로 찾기 등 최단거리를 구해야 할 경우, BFS가 유리하다.
이유 : 왜냐하면 깊이 우선 탐색으로 경로를 검색할 경우 처음으로 발견되는 해답이 최단거리가 아닐 수 있지만, 너비 우선 탐색으로 현재 노드에서 가까운 곳부터 찾기 때문에경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리기 때문입니다.

4) 그 외
- 검색 대상 그래프가 정말 크다면 DFS를 고려
- 검색대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않다면 BFS

## list reference 관련 문제
a = b
둘다 리스트 일시 복사가 아닌 *a=&b가 되어서 (즉 참조가 되어서 )

한곳을 변경하면 나머지 한곳도 변경됌

해결 방안 3가지 방법 존재

1. 한 원소씩 append 혹은 한 원소씩 복사
2. copy()사용 => a=b.copy()
3. slicing  => a=b[:]

+ deepcopy, shallowcopy의 차이점을 알고있도록


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



## zip 함수
python package의 zip
두개이상의 리스트를 받아서
 묶어서 내보내 준다

ex)
a=[1,2,3]
b=[A,B,C]

print(izip(a,b))

=> ((1,A),(2,B),(3,C))

list화 시켜서 활용하도록 하자

## SQL

처리순서 - logic을 이해해볼것
1) FROM
2) ON
3) JOIN
4) WHERE
5) GROUP BY
6) WITH CUBE 또는 WITH ROLLUP
7) HAVING - GROUP절의 조건절
8) SELECT
9) DISTINCT
10) ORDER BY - DESC를 통해 역순가능
11) TOP

예약어에 대한 대소문자는 따로 구분하지 않음 - 통상적으로 대문자로 나타내는것 같음
equal(등호)는 =를 하나만 사용해서 나타낸다.

https://psun.tistory.com/entry/SQL-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC
문법 참고용

- NULL 체크

1) SELECT명령어 IFNULL활용, IFNULL(column, 대체 data)
2)-oracle WHERE명령어 NVL 활용,   NVL(column, 대체data) 주로 대체 data에 0을 넣고 =0으로 찾는경우가많다.
2)-mysql WHERE명령어 IS NULL 활용 
추가로 IS NULL같은경우 case나 if와 활용해서 IFNULL을 대체할수 있으므로 활용도를 높여보자

- JOIN 

https://pearlluck.tistory.com/46

- 서브쿼리

