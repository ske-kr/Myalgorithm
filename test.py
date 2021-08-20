def Problem1(num,k):
    if len(num) <=k:
        return "0"
    
    #check from first
    result=[num[0]]
    for i in num[1:]:
        while k>0 and len(result)>0:
            if result[-1] > i:
                result.pop()
                k-=1
            else:
                break
        result.append(i)
    if k>0:
        result=result[:-k]
    
    Min=""
    for i in result:
        if i=="0" and len(Min)==0:
            continue
        Min+=i
        
    #set corner case
    if Min=="":
        return "0"
    return Min
    
def Problem2(version1,version2):
    #split first
    v1=list(map(int,version1.split(".")))
    v2=list(map(int,version2.split(".")))
    n=abs(len(v1)-len(v2))
    if len(v1)>len(v2):
        for _ in range(n):
            v2.append(0)
    elif len(v1)<len(v2):
        for _ in range(n):
            v1.append(0)
    
    for i in range(len(v1)):
        if v1[i]<v2[i]:
            return -1
        if v1[i]>v2[i]:
            return 1
        
    return 0
        
                   
    
    

def Problem3(s):
    MOD=10**9 + 7
    n=s.count("1")
    if n%3!=0:
        return 0
    if n==0:
        return int((((len(s)-1)*(len(s)-2))/2)%MOD)
    n=n//3
    firstend=0
    secondstart=0
    secondend=0
    thirdstart=0
    #find first part
    for i in range(n):
        firstend=s.find("1")
        s=s[firstend+1:]
        
    
    secondstart=s.find("1")
    
    s=s[secondstart:]
    #find second part
    for i in range(n):
        secondend=s.find("1")
        s=s[secondend+1:]
        
    thirdstart=s.find("1")
    # secondstart means count of 0s between first part and second part
    # so we can add partition between them. same for thirdstart
    
    return int(((secondstart+1)*(thirdstart+1))%MOD)

a=1
print(a//3)


def solution(csv_string, keyword):
    converted=csv_string.split('\n')
    teamname=[]
    member=[0 for _ in range(len(converted))]
    targetteam=[]
    for i in range(1,len(converted)):
        tmp=converted[i].split(",")
        member[i]=tmp[-1]
        if keyword in tmp[1]:
            targetteam.append(tmp[0])
        if tmp[2] in targetteam:
            targetteam.append(tmp[0])
    answer=0
    targetteam=list(set(targetteam))
    for i in targetteam:
        answer+=int(member[int(i)])
    if len(targetteam)==0:
        return -1
    
    return answer


# 조직 ID,조직명,상위 조직 ID,소속 팀원 수
# 1,토스팀,,1
# 2,인터널 트라이브,1,1
# 3,인터널 매니저 팀,2,7
# 4,비바 플랫폼 팀,2,14
# 5,아웃터널 트라이브,1,2
# 6,가이드 팀,5,4
# 7,피트아웃 사일로,5,11

# "아웃"
# 출력예시17

# 한문제를 틀렸는데 왤까?

# 이 때, 특정 검색어로 검색된 조직에 속한 모든 팀원의 수를 반환하는 함수를 작성해주세요.

# 특정 검색어로 검색된 조직이란 다음 2가지 조건 중 하나를 만족하는 조직을 말합니다.

# 조직명이 검색어를 포함
# 위 1번 조건을 만족하는 조직의 하위에 있는 모든 조직
# 만일 위 조건에 따라 검색된 조직이 없다면, 검색에 실패했다는 의미로 -1을 반환해주세요.