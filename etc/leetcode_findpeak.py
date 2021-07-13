# O(n) 으로 구현은 아래처럼 매우 간단하다.
# 그러나 log n이라는 조건이 붙게되면 이때는 다른방법을 사용해야한다
# 대표적으론 binary search가 있다.( cost log(n))

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        tmp=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<tmp:
                return i-1
            tmp=nums[i]
        
        return len(nums)-1

# 아래는 자바로 구현한 binary search code

public class Solution {
    public int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }
    public int search(int[] nums, int l, int r) {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r);
    }
}