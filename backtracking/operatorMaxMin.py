# 14888

n=int(input())
num=list(map(int,input().split()))

operator=list(map(int,input().split()))
Max=-1000000000
Min=1000000000

def dfs(k,tmp):
    global Max
    global Min
    if k==n-1:
        Max=max(Max,tmp)
        Min=min(Min,tmp)
    else:

        for i in range(4):
            if operator[i]!=0:
                operator[i]-=1
                dfs(k+1,operate(i,tmp,num[k+1]))
                operator[i]+=1

                


def operate(i,x,y):
    if i==0:
        return x+y
    if i==1:
        return x-y
    if i==2:
        return x*y
    if i==3:
        if x>=0:
            return x//y
        else:
            return ((-1*x)//y)*(-1)


dfs(0,num[0])
print(Max)
print(Min)