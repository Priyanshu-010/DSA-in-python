nums = [-2,1,-3,4,-1,2,1,-5,4]

# n = len(nums)
# maxi = float("-inf")

# for i in range(n):
#   total = 0
#   for j in range(i, n):
#     total += nums[j]
#     maxi =  max(total, maxi)

# print(maxi)

# Time Complexity: O(n^2), Space complexity: O(1)
# will give TLE not recommended

# Optimal Solution

maxi = float("-inf")
total = 0

for num in nums:
  total += num
  maxi = max(maxi, total)
  if total < 0: # very important remember this
    total = 0

print(maxi)

# Time Complexity: O(n), Space complexity: O(1)

# How this code works:(Simply explained) with this array = [-2,1,-3,4,-1,2,1,-5,4] we will get the maximum subarray sum which is 6

# Explanation of optimized code:

# We initialize two variables maxi and total to keep track of the maximum subarray sum and the current subarray sum, respectively.

# We iterate through the input list nums using a for loop.

# Inside the loop, we update the total variable by adding the current element num to it.

# We update the maxi variable to the maximum of the current total and the previous maxi.

# If the current total is less than 0, we reset the total to 0 to start a new subarray.

# After the loop, we print the maximum subarray sum, which is the final value of the maxi variable.