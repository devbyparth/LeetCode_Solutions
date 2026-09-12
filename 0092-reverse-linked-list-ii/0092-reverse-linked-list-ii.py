class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # 1. Dummy node handles left = 1 seamlessly
        dummy = ListNode(0, head)
        prev = dummy

        # 2. Advance 'prev' to the node right before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # 3. Head-insertion reversal inside the sublist
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next