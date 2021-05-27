import sys

n=int(input())
num=list(map(int,input().split()))
Max=0

def dfs(k,energy):
    global Max
    global num
    if k==n-2:
        if energy>Max:
            Max=energy
    for i in range(1,len(num)-1):
        a=num[:i]
        b=num[i+1:]
        c=[num[i]]
        del num[i]
        dfs(k+1,energy+num[i-1]*num[i])
        num=a+c+b
    
    
    
    
dfs(0,0)
print(Max)