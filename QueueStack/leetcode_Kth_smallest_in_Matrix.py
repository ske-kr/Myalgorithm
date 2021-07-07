## heapq 의 간단한 활용예시
## list형태의 선언후에 활용할수 있다는점이 상당한메리트로 작용한다

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        myheap=[]
        
        for i in matrix:
            for j in i:
                heapq.heappush(myheap,j)
                
        for i in range(k):
            tmp=heapq.heappop(myheap)
        
        
        return tmp