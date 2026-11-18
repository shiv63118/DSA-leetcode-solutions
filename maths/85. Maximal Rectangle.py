class Solution:
    def maximalRectangle(self, matrix):

        if not matrix:
            return 0

        def largestRectangle(heights):

            stack = []
            maximum = 0

            for i in range(len(heights) + 1):

                curr = heights[i] if i < len(heights) else 0

                while stack and heights[stack[-1]] > curr:

                    h = heights[stack.pop()]

                    width = i if not stack else i - stack[-1] - 1

                    maximum = max(maximum, h * width)

                stack.append(i)

            return maximum

        n = len(matrix[0])
        heights = [0] * n

        ans = 0

        for row in matrix:

            for j in range(n):

                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, largestRectangle(heights))

        return ans