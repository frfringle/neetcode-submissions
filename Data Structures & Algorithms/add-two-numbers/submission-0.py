# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        convert_1 = []
        convert_2 = []
        while l1:
            convert_1.append(l1.val)
            l1 = l1.next
        while l2:
            convert_2.append(l2.val)
            l2 = l2.next
        
        sum_1 = 0
        for i in range(len(convert_1)):
            sum_1 += convert_1[i] * 10**i
        sum_2 = 0
        for i in range(len(convert_2)):
            sum_2 += convert_2[i] * 10**i

        converted = str(sum_1 + sum_2)
        length = len(converted)

        ret = ListNode()
        start = ret
        for i in range(length - 1, 0, -1):
            ret.val = int(converted[i])
            ret.next = ListNode()
            ret = ret.next

        ret.val = converted[0]
        return start
        
