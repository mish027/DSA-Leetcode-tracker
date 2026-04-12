# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        dummy.next=head

        prefixSum=0
        seen={0:dummy}
        cur=dummy

        while cur:
            prefixSum+=cur.val
            seen[prefixSum]=cur
            cur=cur.next
        prefixSum=0
        cur=dummy
        while cur:
            prefixSum+=cur.val
            cur.next=seen[prefixSum].next
            cur=cur.next
        return dummy.next

        