from collections import deque
Max=float('inf')

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
def solution(n, s, a, b, fares):
    answer = 0
    costA=[Max for _ in range(n+1)]
    costB=[Max for _ in range(n+1)]
    costS=[Max for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    for i in range(len(fares)):
        graph[fares[i][0]].append([fares[i][1],fares[i][2]])
        graph[fares[i][1]].append([fares[i][0],fares[i][2]])
    
    find_path(costS,graph,s,n)
    print(costS)
    return answer

def find_path(cost,graph,start,n):
    q=deque()
    v=[False for _ in range(n+1)]
    q.append(start)
    v[start]=True
    cost[start]=0
    
    while q:
        tmp=q.popleft()
        v[tmp]=True
        Min=Max
        Next=[]
        for i in range(len(graph[tmp])):
            if v[graph[tmp][i][0]]==False:
                cost[graph[tmp][i][0]]=min(cost[tmp]+graph[tmp][i][1],cost[graph[tmp][i][0]])
                Next.append(graph[tmp][i])
        if len(Next)==0:
            break
        Next.sort(key=lambda x : x[1])
        q.append(Next[0][0])
        del Next[0]

solution(n, s, a, b, fares)