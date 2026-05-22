class Solution:
    def addTwoNumbers(self, l1, l2):

        node1 = l1
        node2 = l2

        n1 = 0
        n2 = 0

        index1 = 1
        index2 = 1

        # linked list -> number
        while node1:
            n1 += node1.val * index1
            index1 *= 10
            node1 = node1.next

        while node2:
            n2 += node2.val * index2
            index2 *= 10
            node2 = node2.next

        result = n1 + n2

        # number -> linked list
        dummy = ListNode(0)
        cur = dummy
        if result == 0:
            return ListNode(0)
        while result > 0:
            dig = result % 10
            cur.next = ListNode(dig)
            cur = cur.next

            result //= 10
        return dummy.next
