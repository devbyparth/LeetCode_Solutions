class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        result = []
        INT_MAX = 2**31 - 1
        
        def backtrack(start: int, path: List[int]) -> bool:
            if start == n:
                return len(path) >= 3
            
            for length in range(1, 11):          # max 10 digits (fits in int32)
                if start + length > n:
                    break
                
                segment = num[start:start + length]
                
                if len(segment) > 1 and segment[0] == '0':   # leading zero
                    break
                
                curr = int(segment)
                if curr > INT_MAX:
                    break
                
                # must match Fibonacci rule once we have 2+ numbers
                if len(path) >= 2:
                    if curr < path[-1] + path[-2]:
                        continue
                    if curr > path[-1] + path[-2]:
                        break                    # numbers only grow — no point trying longer segments
                
                path.append(curr)
                if backtrack(start + length, path):
                    return True
                path.pop()                        # backtrack
            
            return False
        
        backtrack(0, result)
        return result