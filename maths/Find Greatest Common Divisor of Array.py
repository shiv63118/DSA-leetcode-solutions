# 1979. Find Greatest Common Divisor of Array

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(nums[-1], 0, -1):
            if nums[0]%i == 0 and nums[-1]%i == 0:
                return i