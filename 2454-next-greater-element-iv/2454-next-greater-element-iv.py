class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s1, s2 = [], []

        for i, x in enumerate(nums):
            # Resolve 2nd greater element for indices in s2
            while s2 and nums[s2[-1]] < x:
                ans[s2.pop()] = x
            
            # Find indices in s1 that found their 1st greater element (x)
            temp = []
            while s1 and nums[s1[-1]] < x:
                temp.append(s1.pop())

            # Maintain monotonic order by extending s2 in reverse
            s2.extend(reversed(temp))

            # Current index waits in s1 for its 1st greater element
            s1.append(i)

        return ans