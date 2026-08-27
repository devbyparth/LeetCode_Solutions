class Solution:
    def countAndSay(self, n):
        s = "1"

        # Generate terms from 2 up to n
        for _ in range(n - 1):
            next_seq = []
            i = 0
            n_len = len(s)

            # Run-Length Encoding on current string
            while i < n_len:
                count = 1
                # Count consecutive identical characters
                while i + 1 < n_len and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                # Append string representation of count and character
                next_seq.append(str(count))
                next_seq.append(s[i])
                i += 1

            s = "".join(next_seq)

        return s