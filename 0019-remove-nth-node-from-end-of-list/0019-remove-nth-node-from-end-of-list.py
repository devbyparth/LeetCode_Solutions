# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Step 1: Create an (n + 1) step gap between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Step 2: Slide both pointers until fast hits the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Delete the nth node from the end
        slow.next = slow.next.next

        return dummy.next