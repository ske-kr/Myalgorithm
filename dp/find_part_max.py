import sys
input=sys.stdin.readline
#주어진 수열에서 연속하는 부분합중 최대값을 찾는방법
#내방법은 시간복잡도가 너무오래걸림 n^2
#O(n)으로 가능

def main():
    
    n=int(input())

    num=list(map(int,input().split()))
    dp=[0 for i in range(n)]
    dp[0]=num[0]
    for i in range(1,n):
        if num[i]<=0:
            dp[i]=dp[i-1]
        else:
            dp[i]=max(dp[i-1],calldp(num[:i+1]))
    
    print(dp[i])

def calldp(num):#다시
    Max=[]
    Max.append(num[-1])
    for i in range(1,len(num)):
        Max.append(num[-1-i]+Max[i-1])
    return max(Max)


#해당 방법은 너무 비효율적
#아래방법참고
# i번쨰까지의 합은 이전 최적합에 합쳐지던지 혹은 해당 값에서 갱신

def simple(a):
    sum = [a[0]]
    for i in range(len(a) - 1):
        sum.append(max(sum[i] + a[i + 1], a[i + 1]))
    print(max(sum))

#위방법을 최적화

def find_max(arr, num):
    if num == 0:
        return 0
    tot = arr[0]
    max_tot = tot
    for i in range(1, num):
        if tot > 0 and tot + arr[i] >= 0:
            tot += arr[i]
        else:
            tot = arr[i]
        if max_tot < tot:
            max_tot = tot
    return max_tot