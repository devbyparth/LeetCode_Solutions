class Solution(object):
    def maximumProduct(self, nums):
         nums.sort(reverse=True)
         
         n1=nums[0]*nums[1]*nums[2]        
         
         l=len(nums)
         
         n2=nums[l-1]*nums[l-2]*nums[0]
         
         return n1 if n1 >= n2 else n2