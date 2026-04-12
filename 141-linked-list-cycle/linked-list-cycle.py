# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        temp=head
        while temp:

            if temp.val!=float('-Inf'):
                temp.val=float('-Inf')
            else:
                return True
            temp=temp.next
        return False
        