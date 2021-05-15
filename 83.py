class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        else:
            r1 = head
            r2 = r1.next
            while r2 != None:
                if r1.val == r2.val:
                    r3 = r2.next
                    r1.next = r3
                    r2 = r3
                else:
                    r1 = r2
                    r2 = r2.next
        return head
