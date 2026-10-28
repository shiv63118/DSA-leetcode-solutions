class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        max_c = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                count += 1
                if count > max_c:
                    max_c = count
            elif nums[i] == nums[i-1]:
                continue
            else:
                count = 1
        return max_c