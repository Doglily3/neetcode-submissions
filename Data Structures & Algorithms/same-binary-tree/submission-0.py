class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # 两个都空
        if not p and not q:
            return True

        # 一个空一个不空
        if not p or not q:
            return False

        # 值不同
        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )