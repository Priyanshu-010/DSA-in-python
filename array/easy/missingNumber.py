nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

# Brute Force

# for i in range(0, n+1):
#   if i not in nums:
#     print(i)
#     break

# Time Complexity: O(n^2), Space complexity: O(1)

# Better Solution

# freq = {}

# for i in range(0, n+1):
#   freq[i] =0
# for num in nums:
#   freq[num] = 1
# for k,v in freq.items():
#   if v == 0:
#     print(k)
#     break

# Time Complexity: O(n), Space complexity: O(n)

# Optimal Solution

# sum = 0
# for num in nums:
#   sum += num

# print((n*(n+1)//2) - sum(nums)) # You can either use sum func or write a sum Function yourself

# Time Complexity: O(n), Space complexity: O(1)