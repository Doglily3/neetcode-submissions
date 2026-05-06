class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 找中点
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 切开成两个 linked list
        second = slow.next
        slow.next = None

        # 3. reverse 第二段
        prev = None
        cur = second

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        second = prev

        # 4. 合并 first 和 second
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2