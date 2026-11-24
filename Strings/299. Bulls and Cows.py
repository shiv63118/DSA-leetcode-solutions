from collections import Counter

class Solution:
    def getHint(self, secret, guess):

        bulls = 0
        secret_remaining = []
        guess_remaining = []

        for s, g in zip(secret, guess):

            if s == g:
                bulls += 1
            else:
                secret_remaining.append(s)
                guess_remaining.append(g)

        s_count = Counter(secret_remaining)
        g_count = Counter(guess_remaining)

        cows = sum((s_count & g_count).values())

        return f"{bulls}A{cows}B"