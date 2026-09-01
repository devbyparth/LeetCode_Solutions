class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. check karo ki k nodes bache hain ya nahi
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next          # kam nodes → as-is chhod do

            group_next = kth.next

            # 2. group ko reverse karo (prev ko group_next se start karo)
            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3. reconnect
            new_group_prev = group_prev.next   # purana head = naya tail
            group_prev.next = kth              # kth ab is group ka head hai
            group_prev = new_group_prev