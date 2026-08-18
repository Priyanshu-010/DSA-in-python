nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
      # 0 ,1, 2, 3, 4, 5, 6, 7, 8
n = len(nums)

for i in range(1, n):
  key = nums[i]
  j = i -1
  while j >= 0 and key < nums[j]:
    nums[j+1] = nums[j]
    j -= 1
  nums[j+1] = key

print(nums)

# Explanation: The outer loop iterates through the list starting from the second element. The key variable holds the current element to be inserted into the sorted portion of the list. The inner while loop shifts elements in the sorted portion to the right until the correct position for the key is found. Finally, the key is placed in its correct position, resulting in a sorted list.

# In simple words, the insertion sort algorithm builds a sorted list one element at a time by comparing each new element with the already sorted elements and inserting it into its correct position.

# Time complexity: O(n^2), Space complexity: O(1)