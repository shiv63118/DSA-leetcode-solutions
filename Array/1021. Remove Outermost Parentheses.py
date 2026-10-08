class Solution:
    def removeOuterParentheses(self, s):
        ls = []
        sub = ""
        a = 0
        b = 0
        for i in s:
            sub += i
            if i =="(":
                a += 1
            else:
                b += 1

            if a == b:
                ls.append(sub)
                sub = ""
        ans = ""
        for j in ls:
            ans += j[1:-1]

        return ans   

