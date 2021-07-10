a=[1,3,5,7,9]


A=[]
B=[]


Max=0
## 리스트 A에 원소 2개를 집어넣는 루프
for i in range(len(a)):
    A.append(a[i])   # A=[1]
    for j in range(i+1,len(a)):
        A.append(a[j]) # A=[1,5]
        
        ##연산
        tmpA=set(a)
        tmpB=set(A)
        B=list(set(a)-set(A))

        B.sort()
        tmpA=0
        tmpB=0
        for m in range(len(A)):
            tmpA+=A[m]*(10**m)
        for n in range(len(B)):
            tmpB+=B[n]*(10**n)
        tmp=tmpA*tmpB
        print(tmp)
        Max=max(Max,tmp)
        A.pop()
    A.pop()

print(Max)