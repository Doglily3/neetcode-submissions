# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isame(self,root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if not subRoot and root:
            return False
        
        if subRoot.val != root.val:
            return False
        
        return self.isame(root.left,subRoot.left) and self.isame(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        if self.isame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
