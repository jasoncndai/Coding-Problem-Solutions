# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # no extra storage of queues/lists etc.
        # detach linked list into two parts using pointers
        
        if not head:
            return None
        
        # even and odd pointer, even_head to keep track of head of even linkedlist
        odd = head
        even = head.next
        even_head = even
        # "Leap frogging" across the linked list with the pointers hopping from each other
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        # Finally attach end of even linked list to head of odd linked list
        odd.next = even_head
        return head