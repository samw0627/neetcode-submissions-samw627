# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode()
        curr = dummy
        ptr1 = list1
        ptr2 = list2

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                temp = ptr1.next
                curr.next = ptr1
                ptr1 = temp
            else:
                temp = ptr2.next
                curr.next = ptr2
                ptr2 = temp
            curr = curr.next
        curr.next = ptr1 if ptr1 else ptr2
        
        return dummy.next

        
        

         
        