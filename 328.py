class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        r0 = head
        if head == None:
            return head
        r1 = head.next
        sechead = head.next
        if r1 == None:
            return head
        else:
            r2 = r1.next
            if r2 == None:
                return head
            r3 = r2.next
            if r3 == None:
                r0.next = r2
                r0 = r0.next
                r1.next = None
            while r2 and r3 != None:
                r0.next = r2
                r0 = r0.next
                r1.next = r3
                r1 = r1.next
                
                if r1.next != None:
                    r2 = r1.next
                else:
                    break
                if r2.next != None:
                    r3 = r2.next
                else:
                    break
            if r2.next == None and r3 != None:
                r0.next = r2
                r0 = r0.next
                r3.next = None
            r0.next = sechead
        return head  
