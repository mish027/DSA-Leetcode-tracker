# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #approach 3: fast & slow pointer
        '''slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False

        #approach 2: using some value to mark prev nodes
        temp=head
        while temp:

            if temp.val!=float('-Inf'):
                temp.val=float('-Inf')
            else:
                return True
            temp=temp.next
        return False'''
        
        #approach 1: using hashSet

        hashSet=set()
        temp=head
        while temp:
            if temp in hashSet:
                return True
            hashSet.add(temp)
            temp=temp.next
        return False

        