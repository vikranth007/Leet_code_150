# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            g = math.gcd(curr.val, curr.next.val)
            gcd = ListNode(g)
            gcd.next = curr.next
            curr.next = gcd
            curr = gcd.next
        return head
        