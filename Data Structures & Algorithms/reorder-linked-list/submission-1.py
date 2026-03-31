# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Using fast and slow pointers, find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the linked list starting from the slow pointer
        prev = None
        curr = slow.next

        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        ptr1 = head
        ptr2 = prev

        #Merge the two list using 2 pointers
        while ptr1 and ptr2:
            ptr1_next = ptr1.next
            ptr2_next = ptr2.next
            ptr1.next = ptr2
            ptr2.next = ptr1_next
            ptr1 = ptr1_next
            ptr2 = ptr2_next



          
        


        
        