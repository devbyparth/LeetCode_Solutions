class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        avgs = [-1] * n
        window_size = 2*k+1

        if window_size > n:
            return avgs
        
        cur_sum = sum(nums[:window_size])
        avgs[k] = cur_sum // window_size

        for i in range(window_size, n):

            # Naya rightmost element add karo, leftmost purana element hatao
            cur_sum += nums[i] - nums[i - window_size]

            # Center index 'i - k' par result store karo
            avgs[i - k] = cur_sum // window_size

        return avgs