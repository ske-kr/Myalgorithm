#야근시간 최적피로도 구하기
#programmers 검색

#heap의 이상적 사용
#heap은 내부적으로 가장 작은 값이 0 index에 존재하는 트리구조고
# 여기서 -값을 tuple로 넣어준 이유는 당근빳다
# max heap을 만들어주기 위해서 그렇다.(즉 0 index에 최대값이 존재하게 하려고)

import heapq

def solution(n, works):
    answer = 0

    result=[]
    if n>=sum(works):
        return 0
    
    for i in range(len(works)):
        heapq.heappush(result,(-works[i],works[i]))
    # -works[i] 를 넣는 이유는 max heap을 구현하기 위함이다
    while True:
        if n==0:
            break
        tmp=heapq.heappop(result)[1]-1
        
        n-=1
        heapq.heappush(result, (-tmp,tmp))

    for i in result:
        answer+=i[1]*i[1]
    return answer