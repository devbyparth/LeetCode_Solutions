class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        
        # best[i] = length of shortest subarray with sum == target 
        # ending at or before index i
        best = [INF] * n
        
        ans = INF
        left = 0
        window_sum = 0
        
        for right in range(n):
            window_sum += arr[right]
            
            # shrink window while sum exceeds target
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
            
            # carry forward the best length seen so far
            best[right] = best[right - 1] if right > 0 else INF
            
            if window_sum == target:
                curr_len = right - left + 1
                # if there's a valid subarray ending before this window starts,
                # combine it with current window
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, best[left - 1] + curr_len)
                
                # update best[right] with this window's length if it's smaller
                best[right] = min(best[right], curr_len)
        
        return ans if ans != INF else -1