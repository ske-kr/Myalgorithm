# https://leetcode.com/problems/gray-code/solution/ 참고

# one loop solution예시
# O(2^n) 의 답은 다른답도 존재한다.
# 아래 해답은 index값과 해당 gray code 값의 XOR 결과값을 살펴보면 이해할 수 있다.


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i // 2) for i in range(2 ** n)]