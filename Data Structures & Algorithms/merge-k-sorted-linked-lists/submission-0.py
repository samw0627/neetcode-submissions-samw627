# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def merging_list(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val >= list2.val:
                list2.next = merging_list(list1, list2.next)
                return list2
            if list1.val < list2.val:
                list1.next = merging_list(list1.next, list2)
                return list1
        
        currList = lists[0]
        for i in range(1,len(lists)):  
            currList = merging_list(currList,lists[i])
        
        return currList
        


        

        