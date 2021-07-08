# 일반적인 2-d dp활용문제

# 간단했으나 max 부분에서 dp[i][j]를 콜하면 될것을 max(dp[i])로 콜했다-> max를 구하는데 cost 추가소요.

# multi dimension dp를 구현하는데 익숙해져야 할것같다. 


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0]*len(nums2) for _ in range(len(nums1))]
        Max=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
                Max=max(Max,dp[i][j])
                        
        return Max