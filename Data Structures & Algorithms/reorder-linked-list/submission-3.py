# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle of the list
        fast , slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  

        #Reverse the List
        end = slow.next
        slow.next = None #Separate the list 

        prev = None
        curr = end
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #Merge the list together
        dummy1  = ListNode()
        dummy2 = ListNode()
        dummy1.next = head
        dummy2.next  = prev

        p1 = head
        p2 = prev

        while p1 and p2:
            temp1, temp2 = p1.next, p2.next
            p1.next = p2
            p1 = temp1
            p2.next = p1
            p2 = temp2


            



        

        