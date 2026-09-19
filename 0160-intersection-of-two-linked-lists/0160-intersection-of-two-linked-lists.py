class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        temp1, temp2 = headA, headB

        while temp1 != temp2:

            temp1 = temp1.next
            temp2 = temp2.next

            if temp1 == temp2: return temp1

            if temp1 == None: temp1 = headB
            if temp2 == None: temp2 = headA
        
        return temp1