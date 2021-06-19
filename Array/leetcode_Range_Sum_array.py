#흔히 BIT라고 불리는 펜윅 트리(Fenwick Tree)는 
#‘수시로 바뀌는 수열의 구간 합’을 빠르게 구할 수 있도록 고안된 자료 구조이다.
#BIT활용문제 예시
# 먼저 i &-i 연산을 이해해야 한다. 손으로 몇번 해보면 상당히 쉬운데
# 바로 LSB를 구하는 것이다(LSB는 bit단위로 값이 1인것중 가장 낮은자리값)
# 여기서 구한 LSB BIT구조에서는 몇개의 연속된 값이 들어가있냐로 이해하면 쉬울것같다.
# 좀더 간략한 예시
# BIT[1] = Nums[1]
# BIT[2] = Nums[1]+Nums[2]
# BIT[3] =                 Nums[3]
# BIT[4] = Nums[1]+Nums[2]+Nums[3]+Nums[4]
# BIT[5] =                                 Nums[5]
# BIT[6] =                                 Nums[5]+Nums[6]
# 이런느낌이다

# 그렇다면 
# 부분합을 구할때 n이 아닌 logn만 소모하기 때문에 time cost가 훨씬 줄어들 수 있게 된다.

# 값을 수정한다고 하면 대신에 예를들어 1을 수정하면 BIT의 1,2,4,8,16,,,, 을 다수정해야한다.



class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.BIT = [0] + nums[:]
        for i in range(1, self.n + 1):
            j = i + (i & -i)
            if j <= self.n:
                self.BIT[j] += self.BIT[i]

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.n:
            self.BIT[i] += delta
            i += (i & -i)

    def sumRange(self, i: int, j: int) -> int:
        return self.getPrefix(j) - self.getPrefix(i-1)

    def getPrefix(self, i: int) -> int:
        i += 1
        result = 0
        while i > 0:
            result += self.BIT[i]
            i -= (i & -i)
        return result