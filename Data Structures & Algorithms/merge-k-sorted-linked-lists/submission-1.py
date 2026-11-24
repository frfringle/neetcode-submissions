# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        bingle = {}
        lists = list(filter(None, lists))
        if not lists: return 
        for linked in lists:
            while linked:
                bingle[linked.val] = bingle.get(linked.val, 0) + 1
                linked = linked.next
        head = ListNode()
        start = head
        prev = head
        for i, v in dict(sorted(bingle.items())).items():
            for _ in range(v):
                prev = head
                head.val = i
                head.next = ListNode()
                head = head.next
        
        prev.next = None
        return start