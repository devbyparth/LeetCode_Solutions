class Solution(object):
    def pancakeSort(self, arr):
        n = len(arr)
        out = []

        for i in range(n-1, -1, -1):
            max_element = float('-inf')
            idx = 0
            for j in range(i+1):
                if arr[j] >= max_element:
                    idx = j
                    max_element = arr[j]
            
            if idx == i:
                continue
            
            if idx != 0:
                arr[:idx+1] = arr[:idx+1][::-1]
                out.append(idx+1)
            
            arr[:i+1] = arr[:i+1][::-1]
            out.append(i+1)
        
        return out