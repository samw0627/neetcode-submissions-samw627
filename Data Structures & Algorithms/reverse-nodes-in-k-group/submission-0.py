# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Find the kth Node
        dummy = ListNode(0,head)
        groupPrev = dummy #Tail of the previous Group
        while True:
            #Find the kth Node
            kthNode = self.get_kth_node(groupPrev,k)
            if not kthNode:
                break
            groupNext = kthNode.next #Head of the next group

            prev,curr = groupNext, groupPrev.next
            tmp = groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            groupPrev.next = kthNode
            groupPrev =  tmp#Update


        return dummy.next

    def get_kth_node(self, curr,k):
        while curr and k > 0:
            curr = curr.next
            k-= 1
        return curr


            
        
        


        


        


        
        