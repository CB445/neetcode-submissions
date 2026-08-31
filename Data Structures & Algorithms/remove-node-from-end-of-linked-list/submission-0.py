# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        left = dummy
        right = dummy

        # Move right n nodes ahead
        for _ in range(n):
            right = right.next

        # Move both until right reaches the final node
        while right.next:
            left = left.next
            right = right.next

        # Remove the target node
        left.next = left.next.next

        return dummy.next