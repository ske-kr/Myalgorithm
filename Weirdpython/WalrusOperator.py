## 최근에 나온 기능으로 :=  walrus를 닮았다고해서.. 붙여진 이름이다.
## 설명보다는 아래 예시를 보면 쉽게 이해가 될 것이다.

def some_defined_function():
    return 1

x = some_defined_function()
if x==1:
    print("ok")

## 위를 간단하게

if y:=some_defined_function() == 1:
    print("also ok")

## 이런 방식으로 표현하게 해준다고 보면 된다.