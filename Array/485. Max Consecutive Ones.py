def findMaxConsecutiveOnes(nums):
    ans = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
            if count > ans:
                ans = count
        else:
            count = 0
    return ans

nums = [1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0]
print("maximum consecutive ones is :",findMaxConsecutiveOnes(nums))