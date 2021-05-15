class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        r1 = head
        r2 = head
        for i in range(n):
            r2 = r2.next
        if r2 == None:
            head = head.next
        else:
            while r2.next != None:
                r1 = r1.next
                r2 = r2.next
            r1.next = r1.next.next
        return head
