class Solution:
    def isNumber(self, s):
        s = s.strip()

        num = False
        dot = False
        exp = False
        num_after_exp = True

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = True
                if exp:
                    num_after_exp = True

            elif ch in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False

            elif ch == '.':
                if dot or exp:
                    return False
                dot = True

            elif ch in 'eE':
                if exp or not num:
                    return False
                exp = True
                num_after_exp = False

            else:
                return False

        return num and num_after_exp