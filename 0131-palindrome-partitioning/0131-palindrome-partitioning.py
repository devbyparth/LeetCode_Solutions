class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        
        # Precompute palindrome table: is_pal[i][j] = True if s[i..j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    is_pal[i][j] = (length == 2) or is_pal[i + 1][j - 1]
        
        def backtrack(start: int, path: List[str]):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()               # undo
        
        backtrack(0, [])
        return result