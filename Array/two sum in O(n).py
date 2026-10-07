# two sum problem leetcode in time comlexity O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in has:
                return [i, has.get(j)]
            has[nums[i]] = i
