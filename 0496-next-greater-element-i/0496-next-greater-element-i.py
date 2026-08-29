class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Traverse nums2 from right to left
        for item in reversed(nums2):
            # Maintain a monotonic decreasing stack
            while stack and stack[-1] <= item:
                stack.pop()
            
            # If stack has elements, top is the next greater element; otherwise -1
            next_greater[item] = stack[-1] if stack else -1
            
            # Always push the current item onto the stack
            stack.append(item)
        
        # Build the result for nums1 using the map
        return [next_greater.get(num, -1) for num in nums1]