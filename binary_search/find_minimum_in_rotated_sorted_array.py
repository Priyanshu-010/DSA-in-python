# leetcode - 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

nums = [3,4,5,1,2]
n = len(nums)
low = 0
high = n -1
mini = float("inf")
# print("Input array:", nums)

while low <= high:
  mid = (low + high) // 2
  if nums[mid]<= nums[high]:
    mini = min(mini, nums[mid])
    high = mid -1
  else:
    mini = min(mini, nums[low])
    low = mid + 1

print(mini)

# Time complexity: O(log n), Space complexity: O(1)

# Code Explanation:
# 1. We initialize two pointers, low and high, to the start and end of the array, respectively. We also initialize a variable mini to store the minimum value found so far, starting with infinity.
# 2. We enter a while loop that continues as long as low is less than or equal to high.
# 3. Inside the loop, we calculate the mid index as the average of low and high.
# 4. We check if the element at mid is less than or equal to the element at high. If it is, it means the minimum value is in the left half of the array (including mid), so we update mini with the minimum of mini and nums[mid], and move the high pointer to mid - 1.
# 5. If nums[mid] is greater than nums[high], it means the minimum value is in the right half of the array (excluding mid), so we update mini with the minimum of mini and nums[low], and move the low pointer to mid + 1.
# 6. The loop continues until we have narrowed down the search space to find the minimum value. Finally, we print the minimum value found.