#쉬운문제였지만
# dic을 활용하기 좋았던 문제 참고

n=int(input())
s=[]
for i in range(n):
    s.append(input())
dic={}
sets=[]
for i in s:
    for j in i:
        sets.append(j)
set(sets)

for i in sets:
    dic[i]=0

for i in sets:
    tmp=0
    for j in s:
        for k in range(len(j)):
            if j[-k-1]==i:
                tmp+=(10**k)
    dic[i]=tmp

result=sorted(dic.items(),key=lambda x:-x[1])
k=9
final=0
for i in result:
    final+=i[1]*k
    k-=1
print(final)