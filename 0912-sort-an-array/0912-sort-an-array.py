class Solution:
    def mergeArr(self, nums: List[int], left: int, mid: int, right: int, temp: List[int]) -> None:
        i, j, k = left, mid + 1, left

        # Merge elements in sorted order into temp
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        # Copy remaining elements of left subarray
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1

        # Copy remaining elements of right subarray
        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1

        # Copy merged elements back into original array
        for idx in range(left, right + 1):
            nums[idx] = temp[idx]

    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)

        def break_arr(left: int, right: int) -> None:
            if left >= right:
                return

            mid = (left + right) // 2
            break_arr(left, mid)
            break_arr(mid + 1, right)
            self.mergeArr(nums, left, mid, right, temp)

        break_arr(0, len(nums) - 1)
        return nums