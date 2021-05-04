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