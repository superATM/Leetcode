# 160.相交链表   easy 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != None and b != None:
            if a == b:
                return a
            else:
                a = a.next
                b = b.next
        if a == b:
            return None
        elif a != None:
            c = headA
            d = headB
            while a != None:
                c = c.next
                a = a.next
        elif b != None:
            c = headB
            d = headA
            while b != None:
                c = c.next
                b = b.next
        while c != None and d != None:
            if c == d:
                return c
            else:
                c = c.next
                d = d.next
        return None
