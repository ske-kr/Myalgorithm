# 답자체는 상위권이었으나
# 매번 틀리는 실수를 고쳐야할것
# Solution2가 왜틀렸는가를 생각해보자
# python에서 list를 parameter로 옮겨줄땐
# call by reference방식이다. 그렇기 때문에 그 당시의 경로를 답에 저장해준다고하더라도
# 경로가 탐색마다 바뀌게 되면 마지막에 바뀐 경로가 답안에 들어가게 되있을것이다.
# 그럴땐 copy()함수를 활용할것(line 25와 line 44비교)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root,targetSum):
        result=[]
        path=[]
        def dfs(path,node,Sum):
            if node!=None:
                path.append(node.val)
                Sum+=node.val
                if Sum==targetSum and node.left==None and node.right==None:

                    result.append(path.copy())
                    
                dfs(path,node.left,Sum)
                dfs(path,node.right,Sum)
                path.pop()
                Sum-=node.val
        dfs(path,root,0)
        return result

class Solution2:
    def pathSum(self, root,targetSum):
        result=[]
        path=[]
        def dfs(path,node,Sum):
            if node!=None:
                path.append(node.val)
                Sum+=node.val
                if Sum==targetSum and node.left==None and node.right==None:

                    result.append(path)
                    
                dfs(path,node.left,Sum)
                dfs(path,node.right,Sum)
                path.pop()
                Sum-=node.val
        dfs(path,root,0)
        return result