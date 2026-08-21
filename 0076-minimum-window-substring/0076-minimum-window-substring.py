from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        # how many of each character t requires
        required_counts = Counter(t)
        required_unique_chars = len(required_counts)

        # how many of each character our current window has
        window_counts = defaultdict(int)
        satisfied_unique_chars = 0

        best_length = float('inf')
        best_left = 0

        left = 0
        for right, char in enumerate(s):
            # expand: absorb s[right] into the window
            window_counts[char] += 1

            # a character just became "fully satisfied" (not over-counted repeatedly)
            if char in required_counts and window_counts[char] == required_counts[char]:
                satisfied_unique_chars += 1

            # contract: while window covers all of t, try to shrink from the left
            while satisfied_unique_chars == required_unique_chars:
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_left = left

                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in required_counts and window_counts[left_char] < required_counts[left_char]:
                    satisfied_unique_chars -= 1

                left += 1

        return "" if best_length == float('inf') else s[best_left:best_left + best_length]