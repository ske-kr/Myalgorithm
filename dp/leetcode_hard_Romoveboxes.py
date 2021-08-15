## 공식사이트 솔루션, cache를 활용했다.
## 풀었던 문제중 가장 까다로운듯

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if l > r: return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:  # Increase both `l` and `k` if they have consecutive colors with `boxes[l]`
                l += 1
                k += 1
            ans = (k+1) * (k+1) + dp(l+1, r, 0)  # Remove all boxes which has the same with `boxes[l]`
            for m in range(l + 1, r + 1):  # Try to merge non-contiguous boxes of the same color together
                if boxes[l] == boxes[m]:
                    ans = max(ans, dp(m, r, k+1) + dp(l+1, m-1, 0))
            return ans

        return dp(0, len(boxes) - 1, 0)

## 구글링 솔루션, 타임 리밋에러가 걸린다.
## 만약에 여기서 cache 데코레이터를 넣는다면?
## list 는 hashable하지 않다고 에러가 난다.
## @cache vs @lru_cache 알아보기

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)]for _ in range(n)]
        return self.dfs(boxes,dp,0,n-1,0)
    
    def dfs(self,boxes,dp,l,r,k):
        if l > r:
            return 0
        if dp[l][r][k] > 0:
            return dp[l][r][k]
        while l < r and boxes[r] == boxes[r-1]:
            r -= 1
            k += 1
            
        dp[l][r][k] = self.dfs(boxes,dp,l,r-1,0) + (k+1)*(k+1)
        for i in range(l,r):
            if boxes[i] == boxes[r]:
                dp[l][r][k] = max(dp[l][r][k],self.dfs(boxes,dp,l,i,k+1) + self.dfs(boxes,dp,i+1,r-1,0))
        return dp[l][r][k]
