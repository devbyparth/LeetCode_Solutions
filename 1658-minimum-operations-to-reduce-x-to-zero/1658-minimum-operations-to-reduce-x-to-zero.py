class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        t,n,l,s,m=sum(nums)-x,len(nums),0,0,-1
        for r in range(n):
            s+=nums[r]
            while l<n and s>t:s-=nums[l];l+=1
            if s==t:m=max(m,r-l+1)
        return n-m if m>-1 else -1