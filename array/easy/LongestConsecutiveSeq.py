# leetcode: https://leetcode.com/problems/longest-consecutive-sequence/ 128

nums = [100,4,200,1,3,2]

# n = len(nums)
# count = 0
# for i in range(n):
#     num = nums[i]
#     length = 1
#     while num+1 in nums:
#         length +=1
#         num = num+1
#     count = max(count, length)
# print(count)

# Time Complexity: O(n^2), Space complexity: O(1)

# Gives TLE not recommended

# Better Solution

nums.sort()
count = 0
last_small = float("-inf")
longest = 0

for i in range(len(nums)):
  num = nums[i]
  if num -1 == last_small:
    count += 1
    last_small = num
  elif num != last_small:
    count = 1
    last_small = num
  longest = max(longest, count)

print(longest)

# Time Complexity: O(nlogn), Space complexity: O(1)