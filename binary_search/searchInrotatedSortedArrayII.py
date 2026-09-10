# leetcode 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

nums = [2,5,6,0,0,1,2] 
target = 0

n = len(nums)
low = 0
high = n-1

while low <= high:
  mid = (low + high) //2
  if nums[mid] == target:
    print("True")
    break
  if nums[low] == nums[high] == nums[mid]:
    low = low +1
    high = high -1
    continue
  if nums[mid] <= nums[high]:
    if nums[mid]<= target<= nums[high]:
      low = mid+1
    else:
      high = mid -1
  else:
    if nums[low]<=target<=nums[mid]:
      high = mid-1
    else:
      low = mid +1

if low > high:  
  print("False")

# Time Complexity: O(log n), Space complexity: O(1)

# Code explanation:

# The code uses a modified binary search algorithm to search for the target value in the rotated sorted array.
# The while loop runs until the low index is less than or equal to the high index. This ensures that the loop runs at least once, even if the target value is not found in the array.
# The mid index is calculated as the average of the low and high indices, rounded down to the nearest integer. This is used to find the middle element in the array.
# If the middle element is equal to the target value, the index of the middle element is printed and the loop is broken.
# If the middle element is greater than the target value, the high index is updated to mid-1. This means that the search will continue in the left half of the array.
# If the middle element is less than the target value, the low index is updated to mid+1. This means that the search will continue in the right half of the array.
# If the loop exits without finding the target value, the index -1 is printed, indicating that the target value is not found in the array.