class Solution:
  """
    尾插法
  """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        r1 = new_list
        last_node = new_list.next
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                r2 = l1.next
                r1.next = l1
                l1.next = last_node
                l1 = r2
            else:
                r3 = l2.next
                r1.next = l2
                l2.next = last_node
                l2 = r3
            r1 = r1.next
        if l1 == None:
            r1.next = l2
        elif l2 == None:
            r1.next = l1
        new_list = new_list.next
        return new_list
