class Solution:
    def balancedString(self, s):
        n = len(s)
        target = n // 4

        count = {
            'Q': s.count('Q'),
            'W': s.count('W'),
            'E': s.count('E'),
            'R': s.count('R')
        }

        if all(count[c] == target for c in count):
            return 0

        left = 0
        ans = n

        for right in range(n):
            count[s[right]] -= 1

            while all(count[c] <= target for c in count):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1

        return ans