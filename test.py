from collections import deque
import sys
input = sys.stdin.readline

def bfs(n,m,bug):
    f=[[0]*n for _ in range(m)]
    print(f)
    for i in range(bug):
        x,y=map(int,input().split())
        f[y][x]=1
    q=deque()
    cnt=0
    land=0
    trans=[[-1,0],[1,0],[0,1],[0,-1]]
    for i in range(m):
        for j in range(n):
            print(i,j,[m,n])
            if f[i][j]==1:
                land=0
                cnt+=1
                q.append([i,j])
                f[i][j]=0
                while q:
                    land+=1
                    tmp=q.popleft()
                    for i in range(4):
                        n_x=tmp[0]+trans[i][0]
                        n_y=tmp[1]+trans[i][1]
                        if 0<=n_x<m and 0<=n_y<n and f[n_x][n_y]==1:
                            q.append([n_x,n_y])
                            f[n_x][n_y]=0
    print(cnt)

    
n= int(input())
for i in range(n):
    q,w,bug=map(int,input().split())
    bfs(q,w,bug)
