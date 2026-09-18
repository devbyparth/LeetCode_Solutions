class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        
        # Record first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # For each character's first occurrence, try to build a valid interval
        # A valid interval [start, end] must contain ALL occurrences of every
        # character that appears inside it.
        intervals = []
        for i in range(n):
            if first[s[i]] != i:
                continue  # only attempt to start at a character's first occurrence
            
            start, end = i, last[s[i]]
            j = start
            valid = True
            while j <= end:
                c = s[j]
                if first[c] < start:
                    # some occurrence of c lies before our start -> can't be self-contained
                    valid = False
                    break
                if last[c] > end:
                    end = last[c]  # expand the window
                j += 1
            
            if valid:
                intervals.append((start, end))
        
        # Greedy interval scheduling: sort by end, pick earliest-ending
        # non-overlapping intervals (this also minimizes total length,
        # satisfying the tie-breaking rule)
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        
        return res