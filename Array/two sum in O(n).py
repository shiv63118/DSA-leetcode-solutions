# two sum problem leetcode in time comlexity O(n)
class Solution:
    def twoSum(self, nums, target):
        has = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in has:
                return [i, has.get(j)]
            has[nums[i]] = i
            



t = Solution()
nums = [2,9,4,5,6]
target = 10
print(t.twoSum(nums, target))