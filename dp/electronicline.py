import sys
import heapq
input=sys.stdin.readline

n=int(input())
dp=[]
for i in range(n):
    v=list(map(int,input().split()))
    dp.append(v)

dp.sort(key=lambda x:x[0])
a=[0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if dp[j][1]<dp[i][1] and a[j]>a[i]:
            a[i]=a[j]
            
    a[i]=a[i]+1

print(n-max(a))