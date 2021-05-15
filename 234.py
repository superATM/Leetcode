class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        r = []
        while head != None:
            r.append(head.val)
            head = head.next
        for i in range(len(r)//2):
            if r[i] != r[len(r)-i-1]:
                return False
        return True
