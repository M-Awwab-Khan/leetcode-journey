# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return abs(x)

        if head.next == None:
            return head
        else:
            current_node = head
            while current_node.next:
                gcd = computeGCD(current_node.val, current_node.next.val)
                current_node.next = ListNode(gcd, current_node.next)
                current_node = current_node.next.next
        return head