class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        left = dummy
        right = head

        i = 1

        while right:

            if i > n:
                left = left.next

            right = right.next
            i += 1

        left.next = left.next.next

        return dummy.next