# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        if k == length or length == 1:
            return head

        current.next = head

        k = k % length

        first = head
        for i in range(length - k - 1):
            first = first.next

        answer = first.next
        first.next = None

        return answer


        

        