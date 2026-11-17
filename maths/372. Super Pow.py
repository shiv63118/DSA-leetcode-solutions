class Solution:
    def superPow(self, a, b):
        MOD = 1337

        def power(a, k):
            if k == 0:
                return 1

            x = power(a, k // 2)

            x = (x * x) % MOD

            if k % 2:
                x = (x * a) % MOD

            return x

        ans = 1

        for digit in b:
            ans = (power(ans, 10) * power(a, digit)) % MOD

        return ans