nums = [1,1,1,2,3,4,4,7,9,9,9,10]
n= len(nums)

freq= {}
for i in range(0,n):
  freq[nums[i]] = 0

j = 0
for k in freq:
  nums[j] = k
  j+=1

print(nums)
print(len(freq))


# Optimal Solution

# n= len(nums)

# if n == 1:
#   print(n)

# i = 0
# j = i+1

# while j < n:
#   if nums[j] != nums[i]:
#     i += 1
#     nums[i], nums[j] = nums[j], nums[i]
#   j+=1

# print(i+1)
# print(nums)