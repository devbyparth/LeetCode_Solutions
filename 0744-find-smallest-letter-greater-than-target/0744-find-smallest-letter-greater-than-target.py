class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low, high = 0, len(letters) - 1
        ans = letters[0]
        while low <= high:
            mid = (low + high) // 2

            if ord(letters[mid]) > ord(target):
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans