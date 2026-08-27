class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows, counts = 0, 0, [0]*10

        for s_char, g_char in zip(secret, guess):
            if s_char == g_char:
                bulls += 1
            else:
                s_digit = int(s_char)
                g_digit = int(g_char)

                # If s_digit was already seen in guess, it contributes to cows
                if counts[s_digit] < 0:
                    cows += 1
                # If g_digit was already seen in secret, it contributes to cows
                if counts[g_digit] > 0:
                    cows += 1
                
                # Increment count for secret digit, decrement for guess digit
                counts[s_digit] += 1
                counts[g_digit] -= 1
                
        return f"{bulls}A{cows}B"