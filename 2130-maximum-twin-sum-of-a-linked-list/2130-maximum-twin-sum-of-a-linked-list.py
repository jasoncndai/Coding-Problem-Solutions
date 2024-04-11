# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Intuition reverse linked list and use reversed head with forward head to find each sum comparing max
        # reverse second half, use slow and fast pointer to find middle
        head1 = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = self.reverseList(slow)
        
        return self.findMax(head1, head2)
        
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def findMax(self, head1, head2):
        maxSum = 0
        while head1 and head2:
            maxSum = max(maxSum, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
        return maxSum