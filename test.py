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



a="myname is {}"
print(a)
print(a.format("kwangeun"))