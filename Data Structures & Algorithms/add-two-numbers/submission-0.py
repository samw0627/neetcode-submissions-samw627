# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Extract the 2 numbers as array
        num1 = ""
        num2 = ""
        #Traverse the list to extract the numbers
        curr = l1
        while curr:
            num1+= str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next
        
        #reverse the string
        reverse_num1 = num1[::-1]
        reverse_num2 = num2[::-1]

        #Convert to integers
        final = int(reverse_num1) + int(reverse_num2)

        temp = str(final)
        final_str = temp[::-1]
        print(final_str)
        #Create a new linked list
        head = ListNode()
        prev = head
        for c in final_str:
            #Create listNode
            curr = ListNode()
            curr.val = int(c)
            prev.next = curr
            prev = curr
        return head.next
        
            
        



    
        