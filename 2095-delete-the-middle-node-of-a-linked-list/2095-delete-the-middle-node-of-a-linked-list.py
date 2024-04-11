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
        # slow and fast pointer?
        slow = head
        fast = head
        prev = None
        # Fast pointer moves twice as fast, when fast reaches end of linked list
        # prev will be at pointer to middle and slow will be pointer from middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # pointer to middle node changes to pointer from middle node
        prev.next = slow.next
        return head
         
        