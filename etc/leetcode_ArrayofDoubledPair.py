## Counter 예제
## Counter는 이름을 봐도 알 수 있듯이 count한 결과를 반환하는데 이때 dictionary의 형태를 활용해
## 결과를 return한다

## 해당 solution에서는 절대값을 기준으로 sorted된 결과가 필요하기 때문에 sorted( key=abs)를 활용했다
## 참고 - dictionary는 .sort()가 없고 sorted함수를 활용해야한다. 혹은 keys()를 활용해서 list를 선언후
## sort()를 활용할 수 있다.

from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        cnt=Counter(arr)
        
        sorted_cnt=sorted(cnt, key= lambda x:abs(x))
        #key = abs로 간단하게 적어줄 수 있다. 참고
        
        for i in sorted_cnt:
            if cnt[i] <= cnt[i*2]:
                cnt[i*2]-=cnt[i]
            else:
                return False
        
        return True