# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        current = head
        for element in stack:
            if current.val != stack.pop():
                return False
            current = current.next
        return True

