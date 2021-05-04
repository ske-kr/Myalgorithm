from itertools import product
def solution(numbers, target):
    l = [[x, -x] for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

#해당 함수는 주어진 숫자리스트에서 target숫자로 조합가능한 경우의수를 뱉는것
# 여기서 모든 경우의수 곱을 체크해야 하는데
# dfs bfs이외에도 +,-부호를 가진 데이터를 가지고 모든 곱을 계산해주는
# itertools의 product라는 툴이 존재함
# 예를들어 [[1,-1],[2,-2],[3,-3]]을 넣어주면
# [1,2,3] [1,-2,3] [1,2,-3] [1,-2,-3]
# [-1,2,3] [-1,-2,3] [-1,2,-3] [-1,-2,-3] 을 반환한다.
# 그외에도 예를들어 'ABCD' 'xy' 이런걸 넣어주면
# Ax Ay Bx By Cx Cy Dx Dy가 출력됌 개쩐다..