import sys
input=sys.stdin.readline
n=int(input())
v=int(input())

tree=[]
for i in range(n):
    tree.append([])
#graph를 만들어주는 부분, 그래프는 단방향이아니고 bidirection임에 유의하자.
for i in range(v):
    start,end=map(int,input().split())
    tree[start-1].append(end-1)
    tree[end-1].append(start-1)

q=[]
q.append(0)
cnt=0
virus=[ False for _ in range(n)]

while q:
    node=q[0]
    del q[0]
    #bfs방식인데 여기서 중요한점은 1번,2번노드가 queu에 있을때 2번노드를 1번노드에서 다시 호
    #출할수 있으므로 시작전에 다시 체크해줘야한다. 중요
    if virus[node]==True:
        cnt-=1
        continue
    virus[node]=True
    for i in range(len(tree[node])):
        if virus[tree[node][i]]==False:

            cnt+=1
            q.append(tree[node][i])

print(cnt)