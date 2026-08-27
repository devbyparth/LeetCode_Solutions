class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Step 1: Filter valid replacements where source matches s at index
        replacements = {}
        for idx, src, tgt in zip(indices, sources, targets):
            if s.startswith(src, idx):
                replacements[idx] = (len(src), tgt)
        
        # Step 2: Rebuild string sequentially
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            if i in replacements:
                src_len, tgt = replacements[i]
                res.append(tgt)
                i += src_len  # Skip replaced characters
            else:
                res.append(s[i])
                i += 1
                
        return "".join(res)