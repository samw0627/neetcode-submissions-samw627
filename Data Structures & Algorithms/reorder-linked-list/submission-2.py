# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Divide the list into 2 halves
        fast_ptr = head
        slow_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        #Reverse the list from slow_ptr to fast_ptr
        second = slow_ptr.next
        slow_ptr.next = None
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev

        #Merge list 
        ptr1 = head
        ptr2 = prev

        dummy = ListNode()
        dummy.next = ptr1
        while ptr1 and ptr2:
            nxt1 = ptr1.next
            nxt2 = ptr2.next
            
            ptr1.next = ptr2
            ptr2.next = nxt1

            ptr1 = nxt1
            ptr2 = nxt2

            
            

        