class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        dummy = ListNode()
        current = dummy
        ptr1 = list1
        ptr2 = list2

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next

        current.next = ptr1 if ptr1 else ptr2
        
        return dummy.next