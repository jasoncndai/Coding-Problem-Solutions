# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        # pointer for previous and current node
        prev = None
        curr = head
        while curr:
            # next stores next in original linked list
            next = curr.next
            # curr.next becomes previous entry in linked list (reversing step)
            curr.next = prev
            # move prev and current pointers forward
            prev = curr
            curr = next
        return prev