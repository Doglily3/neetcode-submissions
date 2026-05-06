class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode()
        tail = fake_head

        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

        if head1:
            tail.next = head1

        if head2:
            tail.next = head2

        return fake_head.next