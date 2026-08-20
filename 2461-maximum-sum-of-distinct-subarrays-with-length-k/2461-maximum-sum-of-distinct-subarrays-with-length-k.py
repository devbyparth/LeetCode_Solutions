from collections import Counter
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        freq = Counter(nums[:k])
        cur_sum = sum(nums[:k])
        
        # Only set max_sum if the initial window has k unique elements
        max_sum = cur_sum if len(freq) == k else 0
        
        for i in range(k, len(nums)):
            outgoing = nums[i - k]
            incoming = nums[i]
            
            # Add incoming element
            freq[incoming] += 1
            cur_sum += incoming
            
            # Remove outgoing element
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]  # Clean up keys with 0 count
            cur_sum -= outgoing
            
            # Check if current window has k distinct elements
            if len(freq) == k:
                max_sum = max(max_sum, cur_sum)
                
        return max_sum