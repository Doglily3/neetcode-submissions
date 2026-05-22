# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while right.next:
            if i >= n:
                left = left.next
            
            right = right.next
            i += 1
        
        left.next = left.next.next

        return dummy.next
