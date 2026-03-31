# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Using two pointers that is separated by distance n, we can locate the position of the node with slow ptr
        slow = head
        fast = head
        prev = None

        for k in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev is not None:
            prev.next = slow.next
        else:
            head = slow.next
        


        return head
        

        