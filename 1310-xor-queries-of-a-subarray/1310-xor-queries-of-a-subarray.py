class Solution(object):
    def xorQueries(self, arr, queries):
        n = len(arr)
        prefixXor = [0] * (n+1)

        for i in range(n):
            prefixXor[i+1] = prefixXor[i] ^ arr[i]

        result = []
        for left, right in queries:
            result.append(prefixXor[right+1] ^ prefixXor[left])
        
        return result