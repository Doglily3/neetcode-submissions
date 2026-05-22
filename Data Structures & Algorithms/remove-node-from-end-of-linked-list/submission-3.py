class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # fast 走到最后，slow 会停在要删除节点的前一个
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 删除 slow 后面的节点
        slow.next = slow.next.next

        return dummy.next