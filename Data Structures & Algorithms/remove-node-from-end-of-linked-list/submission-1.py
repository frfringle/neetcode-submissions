# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                node.next, prev, node = prev, node, node.next
            return prev

        rev = reverse(head)

        # in the reversed list, the nth-from-end is the nth from the front
        if n == 1:
            rev = rev.next              # drop the first node
        else:
            cur = rev
            for _ in range(n - 2):      # stop at the node before the target
                cur = cur.next
            cur.next = cur.next.next    # actually unlink it

        return reverse(rev)