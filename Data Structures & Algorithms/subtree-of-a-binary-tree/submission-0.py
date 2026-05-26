class Solution:

    def isSame(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSame(p.left, q.left)
            and
            self.isSame(p.right, q.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        # 当前 node 开始是否相同
        if self.isSame(root, subRoot):
            return True

        # 继续往下找
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )