# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp=head
        lenL=0

        while temp:
            lenL+=1
            temp=temp.next

        temp=head
        count=0
        while count<lenL//2:
            count+=1
            temp=temp.next

        return temp
        