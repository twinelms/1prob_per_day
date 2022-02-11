# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            l = 0
            while head:
                head = head.next
                l += 1
            return l
        
        len1, len2 = length(l1), length(l2)

        pre = None
        while len1 or len2:  # 7<=7<=10<=7
            v = 0
            if len1 >= len2:
                v += l1.val
                l1 = l1.next
                len1 -= 1
            if len1 < len2:
                v += l2.val
                l2 = l2.next
                len2 -= 1
            node = ListNode(v)
            node.next = pre
            pre = node
        cur = pre
        carry = 0
        pre = None
        while cur:    # 7 <= 0 <= 8 <= 7
            v = (carry + cur.val)%10
            carry = (carry + cur.val)//10
            node = ListNode(v)
            node.next = pre
            pre = node
            cur = cur.next
        if carry:
            node = ListNode(carry)
            node.next = pre
            pre = node
        return pre
