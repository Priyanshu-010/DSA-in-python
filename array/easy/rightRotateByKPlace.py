nums = [1,2,3,4,5,6,7]
k = 2

# Optimal Solution
n = len(nums)
k = k%n
if k == 0:
  print(nums)
nums[:] = nums[n-k:] + nums[:n-k]

print(nums)

# one more optimal solution

# n = len(nums)
# k = k%n
# if k == 0:
#   print(nums)

# def reverse(nums, left, right):
#   while left<right:
#     nums[left], nums[right]= nums[right], nums[left]
#     left +=1
#     right -=1

# reverse(nums,n-k,n-1) # reverse Last K elements
# reverse(nums,0,n-k-1) # reverse remaining elements
# reverse(nums,0, n-1 ) # reverse the whole array

# print(nums)


# Brute Force

# n = len(nums)
# rotations = k%n
# for _ in range(0, rotations):
#   e = nums.pop()
#   nums.insert(0, e)

# print(nums)