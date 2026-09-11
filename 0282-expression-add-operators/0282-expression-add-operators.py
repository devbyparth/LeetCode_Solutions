class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        result = []
        
        def backtrack(index, path, value, prev):
            if index == n:
                if value == target:
                    result.append(path)
                return
            
            for i in range(index, n):
                segment = num[index:i + 1]
                
                # skip numbers with leading zero (unless it's "0" itself)
                if len(segment) > 1 and segment[0] == '0':
                    break
                
                curr = int(segment)
                
                if index == 0:
                    # first number — no operator before it
                    backtrack(i + 1, segment, curr, curr)
                else:
                    # try +
                    backtrack(i + 1, path + '+' + segment, value + curr, curr)
                    # try -
                    backtrack(i + 1, path + '-' + segment, value - curr, -curr)
                    # try * — undo the previous operand's contribution, then multiply
                    backtrack(i + 1, path + '*' + segment, value - prev + prev * curr, prev * curr)
        
        backtrack(0, "", 0, 0)
        return result