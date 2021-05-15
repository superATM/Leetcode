class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            r1 = head
            r2 = r1.next
            r1.next = r2.next
            r2.next = r1 
            head = r2
            r1.next = self.swapPairs(r1.next)
            return head
