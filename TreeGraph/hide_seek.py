start,end=map(int,input().split())
    
v=[False for _ in range(100001)]    
if start >= end:
    print(start-end)
else:
    cnt=0
    q=[end]
    v[end]=True
    while q:
        if q.count(start)>0:
            print(cnt)
            break
        for i in range(len(q)):
            #check
            tmp=q[0]
            del q[0]
            if tmp%2!=0 and tmp>=1:
                if tmp+1<=100000:
                    if v[tmp+1]==False:
                        q.append(tmp+1)
                        v[tmp+1]=True
                if v[tmp-1]==False:
                    q.append(tmp-1)
                    v[tmp-1]=True
            else:
                if tmp%2==0 and tmp>=1:
                    if tmp+1<=100000:
                        if v[tmp+1]==False:
                            q.append(tmp+1)
                            v[tmp+1]=True
                    if v[tmp-1]==False:
                        q.append(tmp-1)
                        v[tmp-1]=True
                    if v[tmp//2]==False:
                        q.append(tmp//2)
                        v[tmp//2]=True
        cnt+=1