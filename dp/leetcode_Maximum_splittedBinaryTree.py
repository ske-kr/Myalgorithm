class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        Max=[0]
        
        MOD = 10**9 + 7
        
        def dfs(root, total):
            if not root:
                return 0
            subtotal = dfs(root.left, total)+dfs(root.right, total)+root.val
            Max[0] = max(Max[0], subtotal*(total-subtotal) )
            return subtotal

        dfs(root, dfs(root, 0))
        return Max[0] % MOD