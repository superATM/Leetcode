class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = ListNode()
        s1 = head1
        r1 = head
        # 判断首个是空的情况
        if head == None:
            return None
        # 判断head比x小的情况
        while head != None:
            if head.val < x:
                s1.next = head
                head = head.next
                s1 = s1.next
                r1 = head
            else:
                break
        while r1 != None:
            r2 = r1.next
            # 判断r2是尾的情况
            if r2 == None :
                if r1.val < x:
                    s1.next = r1
                    s1 = s1.next
                else:
                    r1 = r1.next
            # 正常判断r2比x小则跳过，并接到新的head1之后
            elif r2.val < x:
                s1.next = r2
                r1.next = r2.next
                s1 = s1.next
            else:
                r1 = r1.next
        s1.next = head
        # head1 跳过空头
        head1 = head1.next
        return head1
