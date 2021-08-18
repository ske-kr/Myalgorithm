print(all([1]))

print(all([False]))

print(all([1,2,3,False]))

print(all([]))
print(all([[]]))
print(all([[[]]]))
print(all([[[False]]]))
print(all([[[]],[[]]]))

## all은 iterable한 객체에서 모두가 true인지 체크하는 함수이다.
## 일단 empty list는 False와 동일한 취급을 받는다는 것을 알 수 있는데
## 그렇다면 아래 5개가 각각 true, false, true,true,true가 나온 이유는 무엇일까
## 일단 두번째가 false가 나온이유는 앞서말한것 처럼 iterable한 객체 안에 empty list가 있고 이는 false 이기 때문에 그렇다
## 그렇다면 [[[]]] 이 True가 된 이유는 True를 판정할때 제일 첫 iterable 한 객체안에 [[]] 가 존재하게 되고
## [[]] 가 empty list가 아니기 때문에 그렇게 판별하게 되는 것이다.(nested list가 되는셈이다) 즉 4번째 예시처럼 false가 들어있다고 한들 판별을 위한
## 최외곽 list속에 empty list가 아닌 무언가가 들어있기 때문에 그렇게 된다.
## all([])이 true라는 것은 외우고 있도록 하자ㅋ..