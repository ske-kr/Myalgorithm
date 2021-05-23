# 9663
# back tracking시 주의할점이 있다
# 간단한 문제의 경우에는 (ex 백준 N과M시리즈)
# append, pop함수를 사용해도 큰 문제가 안생기지만
# 이렇게 경우의수가 늘어날때는 시간이 너무많이 소요되므로
# append,pop함수를 사용할때 조심하도록 하자




n = int(input())
s = [0 for i in range(n)]
result = 0
def isTrue(x):
    for i in range(1, x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
            return False
    return True
# x자리에 놓을수있는지에 대한 체크, 가로축체크와 동시에 대각선체크를함
# 대각선 체크 원리는 x좌표값의 차이의 절대값이 y축좌표값의 차이값과 동일하면
# 동일대각선이므로 False리턴
#그외엔 True리턴

def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n + 1):
            s[cnt] = i
            #y축은 cnt, x축은 i라고생각하고 놓고나서
            #아래 isTrue함수로 놓아지는지 보고 다음단계로 넘어간다
            if isTrue(cnt):
                dfs(cnt + 1)
dfs(1)
print(result)

