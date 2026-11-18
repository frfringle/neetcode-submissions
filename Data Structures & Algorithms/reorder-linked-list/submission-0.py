# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        #find the middle node:
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow is now the value after middle: reverse the end to middle
        l = None
        current = slow.next
        slow.next = None
        while current:
            temp = current.next
            current.next = l
            l = current
            current = temp
        # l is now reversed of the back half
        
        
        start = head
        ret = start
        while l:
            tempslow = start.next
            # need to be able to update fast
            tempfast = l.next
            l.next = start.next
            start.next = l
            
            start = tempslow
            l = tempfast
        