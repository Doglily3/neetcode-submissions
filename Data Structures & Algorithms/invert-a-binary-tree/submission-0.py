class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # 交换左右
        root.left, root.right = root.right, root.left

        # 继续递归
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root