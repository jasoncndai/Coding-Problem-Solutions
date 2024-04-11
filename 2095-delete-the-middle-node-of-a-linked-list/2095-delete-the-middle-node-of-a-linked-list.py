# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Want to delete middle node
        # Problem: don't know length of linked list
        
        # check if linked list is empty or single node
        if not head or not head.next:
            return None
        # slow and fast pointer, start fast one pass in so we get slow to be before middle node rather than after
        slow = head
        fast = head.next.next
        # Fast pointer moves twice as fast, when fast reaches end of linked list
        # slow will be pointer from middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # pointer to middle node changes to pointer from middle node
        slow.next = slow.next.next
        return head
         
        