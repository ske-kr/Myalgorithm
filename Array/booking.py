
n= int(input())
# 예시 문제는 기본 그리디 알고리즘 회의실 예약알고리즘이다.
p=[]
#입출력값으로 여러 인자를 받아야될때
#p=[] 빈 리스트를 선언하고
#p.append(입출력)형식을 이용하거나
#p=[[0]*w for _ in range(n)] 로 n size의 w차원 배열을 선언가능하다.
for i in range(n):
    start,end=map(int,input().split())
    p.append([start,end])

  
p=sorted(p,key=lambda x:x[0]) 
p=sorted(p,key=lambda x:x[1]) 

#p=sorted(p,key=lambda x:(x[0],x[1])) 
#위 방법과 다른점은 아래 방법은 x[0]을 정렬후 해당 x[0]의 sorted순서를 지키면서 x[1]을 정렬할때 사용한다.


# 단순 sort의 경우에는 순서대로 sort하지만 
# sorted, key=lambda를 이용한다면 w차원 배열에서 해당 key값기준으로 sort가능하다
# 다만 sort()는 list의 메소드지만 sorted(list,key)는 python 내장함수이다. 
    
for i in range(n):
    if p[i][0]>=endtime :
        cnt+=1
        endtime=p[i][1]

print(cnt)


