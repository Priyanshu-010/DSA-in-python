nums = [-1,0,3,5,9,12]
target = 0
n =len(nums)
low = 0
high= n-1

# while low <= high:
#   mid = (low+high)//2
#   if nums[mid] == target:
#     print(mid)
#     break
#   elif target > nums[mid]:
#     low = mid+1
#   elif target < nums[mid]:
#     high = mid-1
#   else:
#     print(-1)

# Time Complexity: O(log n), Space complexity: O(1)

# ===============================================================

# Recursive Binary Search

# def bs(nums, low, high,x):
#   if low > high:
#     return -1
  
#   mid = (low+high)//2
#   if nums[mid] == x:
#     return mid
#   elif nums[mid] < x:
#     return bs(nums,mid+1, high,x)
#   else:
#     return bs(nums,low, mid-1,x)

# print(bs(nums,low,high,target))

# Time Complexity: O(log n), Space complexity: O(1)

# ================================================================

# Higher and Lower Bound

# Lower Bound

# lb = n

# while low <= high:
#   mid = (low+high)//2
#   if nums[mid] >= target:
#     lb = mid
#     high = mid-1
#   else:
#     low = mid+1

# print(lb)

# Upper Bound

ub = n

while low <= high:
  mid = (low+high)//2
  if nums[mid] > target:
    ub = mid
    high = mid-1
  else:
    low = mid+1

print(ub)

# Time Complexity: O(log n), Space complexity: O(1)

# ================================================================

# Explanation of Lower and Upper Bound:

# The lower bound is the index of the first element in the array that is greater than or equal to the target value. It is used to find the first occurrence of the target value in the sorted array.
# The upper bound is the index of the first element in the array that is greater than the target value. It is used to find the last occurrence of the target value in the sorted array.

# Code explanation of lower bound:

# The lower bound is the index of the first element in the array that is greater than or equal to the target value. It is used to find the first occurrence of the target value in the sorted array.
# The lower bound is initialized to the length of the array, n. This means that the lower bound is set to the index of the last element in the array.
# The while loop runs until the low index is less than or equal to the high index. This ensures that the loop runs at least once, even if the target value is not found in the array. The loop condition checks if the low index is less than or equal to the high index.
# The mid index is calculated as the average of the low and high indices, rounded down to the nearest integer. This is used to find the middle element in the array.

# If the middle element is greater than or equal to the target value, the lower bound is updated to the mid index, and the high index is updated to mid-1. This means that the search will continue in the left half of the array.
# If the middle element is less than the target value, the low index is updated to mid+1. This means that the search will continue in the right half of the array.
# If the middle element is equal to the target value, the lower bound is set to the mid index, and the search is complete.
# The final value of the lower bound is the index of the first element in the array that is greater than or equal to the target value.

# Code explanation of upper bound:

# The upper bound is the index of the first element in the array that is greater than the target value. It is used to find the last occurrence of the target value in the sorted array.
# The upper bound is initialized to 0, which means that the upper bound is set to the index of the first element in the array.
# The while loop runs until the low index is less than or equal to the high index. This ensures that the loop runs at least once, even if the target value is not found in the array. The loop condition checks if the low index is less than or equal to the high index.
# The mid index is calculated as the average of the low and high indices, rounded down to the nearest integer. This is used to find the middle element in the array.

# If the middle element is greater than the target value, the upper bound is updated to the mid index, and the high index is updated to mid-1. This means that the search will continue in the left half of the array.
# If the middle element is less than or equal to the target value, the low index is updated to mid+1. This means that the search will continue in the right half of the array.
# If the middle element is equal to the target value, the upper bound is set to the mid index, and the search is complete.
# The final value of the upper bound is the index of the first element in the array that is greater than the target value.
