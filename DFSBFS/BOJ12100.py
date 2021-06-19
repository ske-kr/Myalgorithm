## BFS문젠데
## 파이썬 copy의 특징을 공부할수있는문제
## 구현에러도 있긴했지만 스킬이 더 정교해지면 수정할수있을것같음
## https://wikidocs.net/16038 참고

## 예를들어 1차원 list는 copy하면 상관이없지만
## 2-d array같은경우는 2중 list는 여전히 같은 메모리주소를 가리키기때문에
## deep copy를 해야 내부 array 모두 새롭게 copy된다.

import copy

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
cnt=0
Max=0

def move(dir):
    if dir == 0:
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        a[idx][j] = temp

    elif dir == 1:
        for j in range(n):
            idx = n-1
            for i in range(n - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        a[idx][j] = temp

    elif dir == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][idx] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        a[i][idx] = temp

    else:
        for i in range(n):
            idx = n-1
            for j in range(n - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][idx] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        a[i][idx] = temp


def dfs(cnt):
    global n
    global a
    global Max
    if cnt==5:
        for i in range(n):
            Max=max(Max,max(a[i]))
        return
    else:
        for i in range(4):
            tmp=copy.deepcopy(a)
            move(i)
            dfs(cnt+1)
            a=tmp

dfs(0)
print(Max)