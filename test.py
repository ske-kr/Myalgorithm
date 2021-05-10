cnt=0
def dfs():
    global cnt
    if len(queen)==n:
        cnt+=1
    else:
        for i in range(n):
            if queen.count(i)==0 and isTrue(i) :                
                queen.append(i)
                dfs()
                queen.pop()

def isTrue(n):
    for i in range(len(queen)):
        if abs(queen[i]-n)==len(queen)-i:
            return False
    return True


n=int(input())


board=[[0]*n for _ in range(n)]
queen=[]
queen_diagonal=[]

if n==1:
    print(1)
elif n==2:
    print(0)
elif n==3:
    print(0)
else:
    cnt=0
    dfs()
    print(cnt)
