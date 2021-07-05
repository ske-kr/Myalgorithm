# Myalgorithm

자주하는 실수 - 백준

import sys
input = sys.stdin.readline
선언 및 항상 함수형식으로 code를 짤것(속도에서 엄청난 차이가 남)

아주 강력한 툴인 append와 pop은 아주 유용하고 편하지만
수행시간에서 아주 비효율적이다

꼭 써야한다면 특히 append와 del,pop을 사용한다면
deque를 선언해서 사용하자
