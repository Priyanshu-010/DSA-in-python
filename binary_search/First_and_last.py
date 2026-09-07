# Leetcode - 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Brute Force Not required or asked I am just doing it for practice

nums = [5,7,7,8,8,10]
target = 8
# n = len(nums)
# f = -1
# l = -1

# for i in range(n):
#   if nums[i] == target:
#     if f == -1:
#       f = i  # First occurrence
#     l = i 
# print([f,l])


# Optimal Solution - Binary Search

def findBound(isFirst: bool) -> int:
  left, right = 0, len(nums) - 1
  bound = -1
  
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
      bound = mid        # Record the match
      if isFirst:
        right = mid - 1  # Locked on first? Lock leftwards.
      else:
        left = mid + 1   # Locked on last? Look rightwards.
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
          
  return bound

print([findBound(True), findBound(False)])

# Time Complexity - O(log^n) Space complexity - O(1)

# Explanation -
# The code above is a solution to the problem of finding the first and last position of a target element in a sorted array. It uses a binary search approach to efficiently locate the target element and determine its first and last occurrences.
# The function `findBound` takes a boolean parameter `isFirst` to indicate whether we are looking for the first or last occurrence of the target. It initializes two pointers, `left` and `right`, to represent the current search range within the array. The variable `bound` is used to store the index of the found occurrence.
# The while loop continues as long as `left` is less than or equal to `right`.
# The middle index `mid` is calculated as the average of `left` and `right` rounded down to the nearest integer.