"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 무난한 탐색문제
# 다만 time cost를 줄일 여지가 존재한다.

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root==None:
            return []
        result=[]
        q=[]
        
        q.append(root)
        while q:
            result.append([])
            nextq=[]
            for i in q:
                if i != None:
                    result[-1].append(i.val)
                    for node in i.children:
                        nextq.append(node)
            q=nextq
        
        
        return result