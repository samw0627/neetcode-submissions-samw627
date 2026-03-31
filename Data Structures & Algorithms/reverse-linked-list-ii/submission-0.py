# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
            
        
        curr = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        rightPtr = dummy
        nxt = None
        leftPtr = None
        #Move the left pointer
        for n in range(left-1):
            prev= prev.next
        
        leftPtr = prev.next
        
        #Move the right pointer
        rightPtr = dummy
        for m in range(right):
            rightPtr = rightPtr.next
        
        nxt = rightPtr.next
        rightPtr.next = None

        newHead = reverseList(leftPtr)

        prev.next = newHead
        leftPtr.next = nxt
        return dummy.next

        '''
dummy -> 1 -> 2 -> 3 -> 4 -> 5
 |.      |.         |.  |
 prev.   left   right.   next

        '''
        
        
        

        