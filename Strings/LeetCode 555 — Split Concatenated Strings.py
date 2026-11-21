class Solution:
    def splitLoopedString(self, strs):
        strs = [max(s, s[::-1]) for s in strs]
        best = ""

        for i, s in enumerate(strs):
            for part in (s, s[::-1]):
                for k in range(len(part)):
                    candidate = part[k:] + "".join(strs[i+1:]) + "".join(strs[:i]) + part[:k]
                    if candidate > best:
                        best = candidate

        return best