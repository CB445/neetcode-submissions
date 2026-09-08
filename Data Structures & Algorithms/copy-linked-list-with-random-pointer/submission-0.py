"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToCopy = {}

        # First pass: create a copy of every node
        current = head

        while current:
            oldToCopy[current] = Node(current.val)
            current = current.next

        # Second pass: connect next and random pointers
        current = head

        while current:
            copy = oldToCopy[current]

            copy.next = oldToCopy.get(current.next)
            copy.random = oldToCopy.get(current.random)

            current = current.next

        return oldToCopy[head]