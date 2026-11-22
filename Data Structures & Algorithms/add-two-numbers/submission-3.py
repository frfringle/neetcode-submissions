# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l1
        prev = None
        while l1 or l2 or carry:

            if not l1:
                if l2:
                    prev.next = l2
                    l1 = l2
                    l2 = None
                else:
                    prev.next = ListNode(0)
                    l1 = prev.next

            added = l1.val + (l2.val if l2 else 0) + carry
            if added >= 10:
                carry = 1
                added = added % 10
            else:
                carry = 0
            l1.val = added
            
            prev = l1
            l1 = l1.next
            l2 = l2.next if l2 else None
        
        
        return head
            
        
