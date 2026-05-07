class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        cur = second
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        secondhead = pre

        first = head
        while secondhead:
            val1 = first.next
            val2 = secondhead.next

            first.next = secondhead
            secondhead.next = val1

            first = val1
            secondhead = val2




