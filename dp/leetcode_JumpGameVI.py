from collections import deque
#요점은 그때그때 갱신을 해준다는것
#i번째 dp값이 제일 크다면 그 앞자리값들은 다 없애버리면 되므로
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=deque()
        if n==1:
            return nums[0]
        if nums[0]>nums[0]+nums[1]:
            dp.append([0,nums[0]])
            dp.append([1,nums[0]+nums[1]])
        else:
            dp.append([1,nums[0]+nums[1]])
        if n==2:
            return sum(nums)
        if k==1:
            return sum(nums)
        for i in range(2,n):
            if dp[0][0]==i-k-1:
                dp.popleft()
            tmp=nums[i]+dp[0][1]
            while dp and dp[-1][1]<=tmp:
                dp.pop()
            dp.append([i,tmp])
        return dp[-1][1]