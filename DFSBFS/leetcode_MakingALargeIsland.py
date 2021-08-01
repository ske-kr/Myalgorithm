#무난한 dfs문제인데 비효율적인것같다. time cost 상위62퍼, space는 상위 50퍼
#답지도 거의 동일한 방식 코스트도 비슷하다. 상위 답안지를 비교해볼 필요가 있음

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        Landsize=[0]
        v=[[False]*len(grid[0]) for _ in range(len(grid))]
        direction=[[0,-1],[-1,0],[1,0],[0,1]]
        
        
        def dfs(i,j,size):
            size[0]+=1
            grid[i][j]=len(Landsize)
            v[i][j]=True
            for k in range(4):
                nx,ny=i+direction[k][0],j+direction[k][1]
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and v[nx][ny]!=True and grid[nx][ny]==1:
                    dfs(nx,ny,size)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                size=[1]
                if v[i][j]!= True and grid[i][j]==1:
                    grid[i][j]=len(Landsize)
                    v[i][j]=True
                    for k in range(4):
                        nx,ny=i+direction[k][0],j+direction[k][1]
                        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and v[nx][ny]!=True and grid[nx][ny]==1:
                            dfs(nx,ny,size)
                    Landsize.append(size[0])
        
        Max=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    tmp=[]
                    cnt=1
                    for k in range(4):
                        nx,ny=i+direction[k][0],j+direction[k][1]
                        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]!=0:
                            tmp.append(grid[nx][ny])
                    tmp=set(tmp)
                    
                    for k in tmp:
                        cnt+=Landsize[k]
                    Max=max(cnt,Max)
        if Max==0:
            return Landsize[-1]
        return Max