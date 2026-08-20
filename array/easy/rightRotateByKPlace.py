nums = [1,2,3,4,5,6,7]
k = 2

# Optimal Solution
n = len(nums)
k = k%n
if k == 0:
  print(nums)
nums[:] = nums[n-k:] + nums[:n-k]

print(nums)

# Brute Force

# n = len(nums)
# rotations = k%n
# for _ in range(0, rotations):
#   e = nums.pop()
#   nums.insert(0, e)

# print(nums)