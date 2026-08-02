class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False