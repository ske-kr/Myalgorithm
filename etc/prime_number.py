def solution(n):
    answer = 0
    temp=True
    if n==2:
        return 1
    if n==3:
        return 2
    for k in range(2,n+1):
        temp=True
        sq=round(k**0.5)+1
        for i in range(2,sq):
            if k%i==0:
                temp=False
                break
        if temp==True:
            answer+=1

    return answer





# 기초 최적화(루트까지만 진행했다)
# 안쪽 부분만 확인할것 해당 문제는 2~n까지의 소수개수를 출력

def better_solution(n):
    # n이 소수인지 체크)
    if n<2:
        return False
    if n in (2,3):
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    if n<9:
        return True
    
    k,l=5,n**0.5

    while k<=l :
        if n%k ==0 or n&(k+2)==0:
            return False
        k+=6
    
    return True

# 즉 작은 소수들은 2,3에대해서만 체크하고 나머지 숫자에서는 2와 3의 
# 공배수인 6을 기준으로 5부터 체크해나간다

def best_solution(n):
    seive=[False,False]+[True]*(n-1)
    for (i,e) in enumerate(seive):
    # enumerate는 순서와 data를 같이받는다
        if e :
            #아직 소수라면
            k=i*2
            while k <=n:
                seive[k] = False
                k+=i
    
    return [x for (x,y) in enumerate(seive) if y]

# 첫번쨰 문제에 대한 완벽한 답변
# 해당 방법도 range를 정할때 sq값을 이용해서 구하면 좀더 효율적으로가능하다
