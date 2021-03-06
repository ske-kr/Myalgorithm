class Solution(object):
    def findIntegers(self, num):
        """
        Time : O(1)
        Space : O(1)??

        """
        dp = [0] * 32
        dp[0], dp[1] = 1, 2
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        result, prev_bit = 0, 0
        for i in reversed(range(31)):
            if (num & (1 << i)) != 0:
                result += dp[i]
                if prev_bit == 1:
                    result -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1