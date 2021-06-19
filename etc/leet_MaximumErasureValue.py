##leetcode Maximum erasure value문제
##array를 한번씩 훑어가면서 갱신
## right,left값을 따로설정해서 문제를푸는것으로
## 연속하는 증가수열문제랑 비슷해보이지만
## mapping을 해서 문제를 풀어야한다.

nums=[5,2,1,2,5,2,1,2,5]
mymap=[0 for _ in range((10**4)+1)]
left_index=0
Max=0
dp=0
for right_index in nums:
    mymap[right_index]+=1
    dp+=right_index
    while mymap[right_index]>1:
        mymap[nums[left_index]]-=1
        dp-=nums[left_index]
        left_index+=1
            
    Max=max(Max,dp)


                
    
print(Max)