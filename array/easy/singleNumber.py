nums= [2,2,1]

n = len(nums)

# Brute Force this will give TLE Error Not recommended

# for i in range(n):
#     count = 0
#     # Scan the ENTIRE array
#     for j in range(n):
#         if nums[i] == nums[j]:
#             count += 1
    
#     if count == 1:
#         print(nums[i])

# Time Complexity: O(n^2), Space complexity: O(1)

# Better Solution

# freq = {}
# for i in range(0, n):
#   if nums[i] in freq:
#     freq[nums[i]] += 1
#   else:
#     freq[nums[i]] = 1

# for k,v in freq.items():
#   if v == 1:
#     print(k)

# Time Complexity: O(n), Space complexity: O(n)

# OPtimal Solution

result = 0
for num in nums:
    result ^= num  # XOR accumulates
print(result) # result

# Time Complexity: O(n), Space complexity: O(1)

# Explanation of this code: 

# We initialize a variable result to 0, which will be used to store the result of the XOR operation.

# We iterate through the input list nums using a for loop.

# For each iteration, we XOR the current element nums[i] with the current value of result.

# After the loop, the final value of result contains the single element that appears once in the list.

# Finally, we print the value of result, which is the single element that appears once in the list.