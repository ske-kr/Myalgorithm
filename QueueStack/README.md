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


import heapq


heapq를 쓰는방식은

list선언후

heapq함수를 통해 집어넣는것이다

기본적으로 heapq는 min heap구조
a=[]

heapq.heappush(a,data)
여기서 data는 tuple형태도 가능하다
(예를 들어 Max힙을 구현하기위해)


(-data,data를 집어넣을수도 있다는 뜻이다)
#heap의 이상적 사용
#heap은 내부적으로 가장 작은 값이 0 index에 존재하는 트리구조고
# 여기서 -값을 tuple로 넣어준 이유는 당근빳다
# max heap을 만들어주기 위해서 그렇다.(즉 0 index에 최대값이 존재하게 하려고)
