# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## classic duplicate check algorithm
        nodes = set()
        current_node = head
        while current_node:
            if current_node in nodes:
                return True
            else:
                nodes.add(current_node)
            current_node = current_node.next
        return False
        ## Tortoise and hare algorithm
        # fast = head
        # while fast and fast.next:
        #     head = head.next
        #     fast = fast.next.next
        #     if head is fast:
        #         return True
        # return False

