import time
## https://www.youtube.com/watch?v=9gEX7jesV34&t=50s

## 유의미한 차이를 보인다고는 할 수 있지만 사실 또 그렇게 큰 차이라고 볼 순 없을듯?
## 비슷한 예시로 x**2가 x*x보다 느리다는 것도 있다.

def notnot(a):
    return not not a

def boolbool(a):
    return bool(a)

Check=True
A=time.time()

for i in range(100000):
    boolbool(Check)

B=time.time()

for i in range(100000):
    notnot(Check)

C=time.time()

print(B-A,C-B)


## "If you care about your python performance - don't use Python"
## That and similar phrase are the answer to many pythong performance questions.
## 재미있는 댓글