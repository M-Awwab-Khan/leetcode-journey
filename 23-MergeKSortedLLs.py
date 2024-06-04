# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for lst in lists:
            current_node = lst
            while current_node:
                result.append(current_node.val)
                current_node = current_node.next
        if result:
            result.sort()
            head = ListNode(result[0])
            current_node = head
            for i in result[1:]:
                current_node.next = ListNode(i)
                current_node = current_node.next

            return head
        return None