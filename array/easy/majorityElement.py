nums = [2,2,1,1,1,2,2]

# n = len(nums)
# max = n //2
# for i in range(n):
#   val = nums[i]
#   count = 0
#   for j in range(n):
#     if nums[i] == nums[j]:
#       count +=1
  
#   if count > max:
#     print(val)
#     break # return val

# print("not found")

# Time Complexity: O(n^2), Space complexity: O(1)
# This gives TLE error so not recommended use hash map instead

# Optimal Solution

counts = {}
threshold = len(nums) // 2

for num in nums:
  counts[num] = counts.get(num, 0) + 1
  if counts[num] > threshold:
    print(num) # return num

# Time Complexity: O(n), Space complexity: O(n)

# In this method we are using hash map to store the freq of each element in the array and then we are checking if the freq of any element is greater than threshold if it is then we are printing that element