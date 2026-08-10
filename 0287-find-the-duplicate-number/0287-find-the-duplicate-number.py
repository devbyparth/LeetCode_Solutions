class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow