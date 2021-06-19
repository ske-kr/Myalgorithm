## 비트마스크형식의 문제풀이
## logical하게 bit형식으로 모든 점을 바꿔서 
## 연산작업을 시행 - 훨씬 간단하게 풀린다(수행시간의 관점에서)
## 내방식은 모든방법을 다체크했으므로 수행시간이 초과

## dfs방식으로 구현해서 pypy3으로 돌리면 어짜피 통과되긴함

# 아래 예시로 설명하자면
# 각 알파벳을 bit단위로 변환( ord함수를 이용해서) <<시키면 2진수number에 자리수에 맞춰서 변환됌

# 그렇게 한 후 combination을 통해
# 배운 알파벳과 각 learnlist의 남은 알파벳을 ^(exclusive or)시켜서
# 만약 0이라면 다 배운거기 때문에 cnt+=1
# 그리고 cnt를 출력하면 될것이다.
## 1위 풀이가 좀 더 간결하고 직관적이다.


import sys
from itertools import combinations
input=sys.stdin.readline
def change(temp):
    res=[]
    for i in temp:
        res.append(ord(i)-ord('a'))
    return res

ans=0
poss=0
n,k=map(int,input().split())
if k>=5:
    num=set()
    data=[]
    for i in range(n):
        t=change(set(input().rstrip()[4:-4])-set(['a','n','i','t','c']))
        if len(t)==0:
            poss+=1
            continue
        num|=set(t)
        data.append(t)
    for i,r in enumerate(data):
        q=0
        for a in r:
            q|=(1<<a)
        data[i]=q
    temp=0
    temp|=1<<(ord('a')-ord('a'))
    temp|=1<<(ord('n')-ord('a'))
    temp|=1<<(ord('t')-ord('a'))
    temp|=1<<(ord('i')-ord('a'))
    temp|=1<<(ord('c')-ord('a'))
    if len(num)<k-5:
        print(n)
    else:
        for i in combinations(num,k-5):
            t=temp
            cnt=0
            for j in i:
                if not t&(1<<j):
                    t|=1<<j
            t^=(1<<26)-1
            for d in data:
                if d&t==0:
                    cnt+=1
            ans=max(ans,cnt)
        print(ans+poss)
else:
    print(0)


#아래는 내방식

import sys
from itertools import combinations

input=sys.stdin.readline
n,k=map(int,input().split())
sen=[]
for i in range(n):
    sen.append(input())
def sol():
    global k
    if k <5:
        print(0)
        return    
    learn=['a','n','t','i','c']
    learn=set(learn)
    learn_list=[]
    for i in sen:
        tmp=set(list(i))
        tmp=tmp-learn
        learn_list.append(tmp)
        learn_list[-1].remove('\n')
    left=k-5
    Max=0
    if left==0:
        for i in learn_list:
            if len(i)==0:
                Max+=1
    else:
        tmp={}
        tmp=set(tmp)
        for i in learn_list:
            if len(i)<=left:
                tmp=tmp|i
        checklist=list(combinations(tmp,left))
        for i in checklist:
            cnt=0
            for j in learn_list:
                if len(j-set(i))==0:
                    cnt+=1
            if cnt>Max:
                Max=cnt
    print(Max)

sol()


## 백준 수행시간1위 풀이

from itertools import combinations
N,K=map(int,input().split())
# 가장 먼저 K값에 따라서 분류
if K<5:
    print(0)
    exit(0)
elif K==26:
    print(N)
    exit(0)
# 5개의 단어는 무조건 익혀야 하므로 -5해준다.
K-=5

# 모든 단어는 "anta"와 "tica"가 포함되어 있다.
# a,n,t,i,c 5개의 단어가 포함된다.
baseset=set('antic')
convert={chr(ord('a')+i):1<<i for i in range(26)}
words=[]
check=set()
ans=0
for _ in range(N):
    # 시작단어, 끝단어 제거
    word=set(input())-baseset
    # 5개의 단어로 읽을 수 있으면 ans +1
    if len(word) == 0:
        ans+=1
    # 배울 수 있는 단어보다 word의 길이가 같거나 짧은것만 읽을 수 있다.
    elif len(word) <= K:
        tmp=0
        # bit로 변환하여 저장
        for s in word:
            tmp +=convert[s]
        words.append(tmp)
        # 배워야 하는 단어의 후보군을 저장
        check |=word

check_size=len(check)
# 후보군을 bit로 변환한다.
check=map(lambda x: convert[x] ,check)
def compare(w):
    # 후보군의 전체 집합
    teach=sum(w)
    result=0
    # 각 단어들과 비교하여 읽을 수 있는지 counting한다.
    for word in words:
        if teach & word == word:
            result+=1
    return result

plus=max(map(compare,combinations(check,min(K,check_size))))
ans+=plus
print(ans)