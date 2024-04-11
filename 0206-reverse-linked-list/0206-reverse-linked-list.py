# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive
        # Base case
        if not head or not head.next:
            return head
        # head recursion, start at the end of the linked list and work backwards
        newHead = self.reverseList(head.next)
        # head.next.next refers to pointer pointing to last node in linked list due to base case returning head = end
        # head.next.next is the pointer from last node to None, point it back to current node that is second last
        head.next.next = head
        # removes the old pointer original pointer before returning new head from last node to second last node
        head.next = None
        return newHead