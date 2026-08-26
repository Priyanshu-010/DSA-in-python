# leetcode link: https://leetcode.com/problems/rearrange-array-elements-by-sign/ 2149
nums= [3,1,-2,-5,2,-4]

# pos = []
# neg = []
# n = len(nums)
# result = []
# for num in nums:
#     if num > 0:
#         pos.append(num)
#     else:
#         neg.append(num)

# # Merge the two arrays taking one element from each array at a time one from positive and then one from negative and so on
# for i in range(len(pos)):
#     result.append(pos[i])
#     result.append(neg[i])

# print(result)

# Time Complexity: O(n), Space complexity: O(n)

# In this code I have used two arrays to store positive and negative numbers. Then I have appended the positive numbers to the result array followed by the negative numbers. This approach ensures that the positive and negative numbers are interleaved in the result array.


# Optimal Solution

n = len(nums)

result = [0]*n

pos= 0
neg = 1

for i in range(0, n):
  if nums[i]>=0:
    result[pos] = nums[i]
    pos+=2
  else:
    result[neg] = nums[i]
    neg+=2


print(result)

# Time Complexity: O(n), Space complexity: O(n)
