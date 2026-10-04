###  PROBLEM ::  MAXIMUM SUBARRAY SUM

nums = [-2,1,-3,4,-1,2,1,-5,4]

n = len(nums)
maximum = float('-inf')

#### brute force approach

# for i in range(n):
#     for j in range(i, n):                   
#         sum  = 0
#         for k in range(i, j+1):
#             sum += nums[k]
#         maximum =  max(maximum, sum)      
# print("maximum :",maximum)

### Better approach 

# for i in range(n):
#     sum  = 0
#     for j in range(i, n):
#         sum += nums[j]
#         maximum = max(maximum, sum)      
# print("maximum :",maximum)

### Optimal approach / optimal solution / Kadane's Algorithm

sum = 0
for i in range(n):
    sum += nums[i]
    maximum = max(maximum, sum)
    if sum < 0:
        sum = 0
print("maximum :",maximum)
    