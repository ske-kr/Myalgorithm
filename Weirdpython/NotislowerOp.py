x=True
y=False

print(not x == y)
## 간단한 원리이다.
## 이는 사실 우리가 not x => False이고 False==False가 된다고 이해하기 쉽지만
## not은 우선순위가 낮기 때문에 x==y => False이고
## not False기 떄문에 True가 return 된다.

## 그렇기 때문에 아래 코드는 에러가 발생한다

# print(x == not y)