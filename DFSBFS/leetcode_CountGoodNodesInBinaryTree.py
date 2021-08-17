## dfs를 활용한 노드카운팅 문제
## bfs를 활용할수 있나?
## Maximum node value값을 갱신하면서 탐색해야 하기 때문에
## 지금생각해보니 q에 root,Max를 같이집어넣는 식이기 때문에 bfs도 마찬가지로 활용할 수 있다 

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt=[0]
        Max=root.val
        def dfs(node,Max):
            if node.val>=Max:
                cnt[0]+=1
            Max=max(Max,node.val)
            if node.left!=None:
                dfs(node.left,Max)
            if node.right!=None:
                dfs(node.right,Max)
            
        dfs(root,Max)
        
        return cnt[0]