# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Leetcode 33. Search in Rotated Sorted Array

# The brute force approach is to iterate through the array and check if the target value is present in the array or not. The time complexity of this approach is O(n) and space complexity is O(1). It's just linear seaching through the array.

nums = [4,5,6,7,0,1,2]
target = 0

n = len(nums)
low = 0
high = n-1

while low <= high:
  mid = (low +high) //2
  if nums[mid] == target:
    print(mid)
    break
  elif nums[mid] <= nums[high]:
    if nums[mid]<=target<=nums[high]:
      low = mid+1
    else:
      high = mid -1
  else:
    if nums[low]<= target <= nums[mid]:
      high = mid -1
    else: 
      low = mid+1

if low > high:
  print(-1)

# Time Complexity: O(log n), Space complexity: O(1)

# Code explanation:

# The code implements a binary search algorithm to search for a target value in a rotated sorted array.
# The low and high pointers are initialized to the first and last index of the array, respectively.
# The while loop runs until the low index is less than or equal to the high index. This ensures that the loop runs at least once, even if the target value is not found in the array.
# The mid index is calculated as the average of the low and high indices, rounded down to the nearest integer. This is used to find the middle element in the array.
# If the middle element is equal to the target value, the index of the middle element is printed and the loop is broken.
# If the middle element is greater than the target value, the high index is updated to mid-1. This means that the search will continue in the left half of the array.
# If the middle element is less than the target value, the low index is updated to mid+1. This means that the search will continue in the right half of the array.
# If the loop exits without finding the target value, the index -1 is printed, indicating that the target value is not found in the array.

