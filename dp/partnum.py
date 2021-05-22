#부분수열문제 11053, 11054 
#

n=int(input())

a=list(map(int,input().split()))
a_reverse=a[::-1]

dp_forward=[0 for i in range(n)]
dp_reverse=[0 for i in range(n)]
dp_total=[0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[j]<a[i] and dp_forward[j]>dp_forward[i]:
            dp_forward[i]=dp_forward[j]
            
    dp_forward[i]=dp_forward[i]+1
##여기까지는 그냥 제일 긴 부분수열구하는것


for i in range(n):
    for j in range(i):
        if a_reverse[j]<a_reverse[i] and dp_reverse[j]>dp_reverse[i]:
            dp_reverse[i]=dp_reverse[j]
            
    dp_reverse[i]=dp_reverse[i]+1

for i in range(len(dp_total)):
    dp_total[i]=dp_forward[i]+dp_reverse[-1-i]

# 역산을 해준이유는 bidirection으로 구하기 위해서, 즉 단방향 제일긴 부분수열은 윗부분만 돌려서 max를 뽑으면 된다.

print(max(dp_total)-1)