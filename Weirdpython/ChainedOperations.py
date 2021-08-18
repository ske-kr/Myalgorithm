print((1==1) in [1])
## True == 1   => True값을 가진다. 즉 True는 1로 취급될 수 있다
print(1==(1 in [1]))

print(1 <(0<1))

print(1<0<1)
## 그렇다면 False는 0으로 취급될 것이고 위의 식은
## False < 1이라는 명제가 되는데 그럼 True를 뱉어야하는게 아닌가?
## python에서는 1<0<1 이라는 식은 1<0 and 0<1로 해석되기 때문이다!

## True, True, False,False 이다.