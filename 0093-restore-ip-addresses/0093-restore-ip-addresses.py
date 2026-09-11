class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        
        if n < 4 or n > 12:          # quick reject — impossible lengths
            return result
        
        def is_valid(segment: str) -> bool:
            if len(segment) > 1 and segment[0] == '0':   # leading zero
                return False
            return int(segment) <= 255
        
        def backtrack(start: int, parts: List[str]):
            if len(parts) == 4:
                if start == n:                # used up the whole string
                    result.append('.'.join(parts))
                return
            
            # each segment can only be 1, 2, or 3 digits long
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if is_valid(segment):
                    parts.append(segment)
                    backtrack(start + length, parts)
                    parts.pop()               # backtrack
        
        backtrack(0, [])
        return result