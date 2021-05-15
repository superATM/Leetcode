class Solution:
  """
    头插法反转
  """
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        while head != None:
            r1 = head
            r2 = r1.next
            r1.next = new_head.next
            new_head.next = r1
            head = r2
        return new_head.next
