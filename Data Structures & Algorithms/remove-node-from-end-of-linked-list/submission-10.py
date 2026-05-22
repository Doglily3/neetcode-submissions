class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # 一起走
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除
        slow.next = slow.next.next

        return dummy.next