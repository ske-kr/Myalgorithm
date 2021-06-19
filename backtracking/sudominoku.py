##4574
##세심하게 살펴볼것
## boj 수행시간 1등 solution 참고용

di = (1, 0)
dj = (0, 1)


# (i,j) 위치에 num을 놓을 수 있는가?
def is_possible(i, j, num):
    if check_row[i][num] or check_col[j][num] or check_sq[(i // 3) * 3 + j // 3][num]:
        return False
    return True


def check(i, j, num, mark):
    check_row[i][num] = check_col[j][num] = check_sq[(i // 3) * 3 + j // 3][num] = mark


def go(row, col):
    # 다음 타일
    i, j = row, col
    while row < 9:
        j += 1
        if j == 9:
            i += 1
            j = 0
        if i >= 9:
            return True
        if greed[i][j] == 0:
            break

    # 어떤 타일을 놓을 수 있는가
    for num1 in range(1, 10):
        if not is_possible(i, j, num1):
            continue
        check(i, j, num1, True)
        greed[i][j] = num1
        for k in range(2):
            ni, nj = i + di[k], j + dj[k]
            if not (0 <= ni < 9 and 0 <= nj < 9) or greed[ni][nj] != 0:
                continue
            for num2 in range(1, 10):
                if num1 == num2 or tile[num1][num2]:
                    continue
                if not is_possible(ni, nj, num2):
                    continue
                check(ni, nj, num2, True)
                greed[ni][nj] = num2
                tile[num1][num2] = tile[num2][num1] = True
                if go(i, j):
                    return True
                tile[num1][num2] = tile[num2][num1] = False
                check(ni, nj, num2, False)
                greed[ni][nj] = 0
        check(i, j, num1, False)
        greed[i][j] = 0
    return False
## 잘 살펴보면 2중 dfs문이 있다고 보면 될것같다.
## 하나를 놓고 나머지 한자리를 놓을수있냐 확인하고
## 마저 놓고 다음으로 진행 이과정에서 True, False로 놓는다는건 참신한발상

tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    greed = [[0] * 9 for _ in range(9)]
    # 백트래킹을 위한 check
    check_row = [[False] * 10 for _ in range(9)]  # i번째 row일때 해당 숫자 가능한가
    check_col = [[False] * 10 for _ in range(9)]  # j번째 col일때 해당 숫자 가능한가
    check_sq = [[False] * 10 for _ in range(9)]  # i*3+j번째 사각형에 해당 숫자 가능한가
    # 사용 타일 체크를 위한 리스트
    tile = [[False] * 10 for _ in range(10)]  # (x,y) 타일 가능한가?

    for _ in range(n):
        temp = input().split()
        i1, j1, num1 = ord(temp[1][0]) - ord('A'), int(temp[1][1]) - 1, int(temp[0])
        i2, j2, num2 = ord(temp[3][0]) - ord('A'), int(temp[3][1]) - 1, int(temp[2])
        greed[i1][j1] = num1
        greed[i2][j2] = num2
        check(i1, j1, num1, True)
        check(i2, j2, num2, True)
        tile[num1][num2] = tile[num2][num1] = True

    ##enumerate의 활용!
    for num, temp in enumerate(input().split(), start=1):
        i, j = ord(temp[0]) - ord('A'), int(temp[1]) - 1
        greed[i][j] = num
        check(i, j, num, True)

    # 시작 col가 -1인 이유는 row값을 받고 column값을 늘려가면서 체크 프로세스를 진행하기 때문에
    go(0, -1)
    print(f"Puzzle {tc}")
    for line in greed:
        print(''.join(map(str, line)))
    tc += 1