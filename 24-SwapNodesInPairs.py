# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        prev = ListNode()
        prev.next = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return prev.next
