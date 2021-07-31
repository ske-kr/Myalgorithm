#간단해보이는 문제지만 생각보다 이해하는데 조금 걸림
# 마찬가지로 left, right index설정후 탐색시작



class Solution:
    def trap(self,height):
        if len(height)<3:
            return 0
        water=0
        
        left,right=0,len(height)-1
        
        max_l,max_r=height[left],height[right]
        
        while left<right:
            max_l=max(max_l,height[left])
            max_r=max(max_r,height[right])
            
            if max_l <= max_r:
                water+= max_l-height[left]
                left+=1
            else:
                water+= max_r-height[right]
                right-=1
        return water

