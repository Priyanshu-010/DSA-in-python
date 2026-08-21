nums = [0,1,0,3,12]

# Not optimal and not in place

# n = len(nums)
# nonZeroes = []
# zeroes = []

# for num in nums:
#   if num == 0:
#     zeroes.append(num)
#   else:
#     nonZeroes.append(num)

# nums = nonZeroes + zeroes

# Time Complexity: O(n), Space complexity: O(n)

# Brute Force

# temp = []
# for num in nums:
#   if num != 0:
#       temp.append(num)
    
# n = len(temp)
# j = 0
# for i in range(0, n):
#   nums[i]= temp[j]
#   j+=1
# for k in range(j, len(nums)):
#   nums[k] = 0

# Time Complexity: O(n), Space complexity: O(n)


# Optimal Solution

n = len(nums)
if n == 1:
  print(nums)

i = 0

while i <n:
  if nums[i] == 0:
    break
  i+=1

if i == n:
  print(nums)

j = i+1

while j < n:
  if nums[j] != 0:
    nums[i], nums[j] = nums[j], nums[i]
    i+=1
  j+=1

# Time Complexity: O(n), Space complexity: O(1)

print(nums)


