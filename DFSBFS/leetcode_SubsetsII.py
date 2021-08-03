#무난한 dfs문제
# combinations로 계산될줄알았지만 예전 비슷한문제와 마찬가지로 [1,4] , [4,1]이 서로 동일하다고
#인식하게 만드는 방법이 없다(sort하면 되지않을까 싶었지만 sort시키면 cost가 너무늘어남)

class Solution(object):
    def subsetsWithDup(self, nums):

        def dfs(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(nums, i+1, path + [nums[i]], res)
            
        res = []
        nums.sort()
        dfs(nums, 0, [], res)
        return res