# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

    cur=TreeNode(preorder.pop(0))
    if inorder.index(cur.val)>0:
        cur.left=self.buildTree(preorder,inorder[:inorder.index(cur.val)])
    if inorder.index(cur.val)<len(inorder)-1:
        cur.right=self.buildTree(preorder,inorder[inorder.index(cur.val)+1:])
            
        
    return cur