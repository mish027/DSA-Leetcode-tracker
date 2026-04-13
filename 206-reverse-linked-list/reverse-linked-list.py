# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def R(head):
            if head==None:
                return head
            if head.next==None:
                return head
            
            p=head
            l=R(head.next)
            p.next.next=p
            p.next=None
            return l
        return(R(head))
            
            
            
        

      
    