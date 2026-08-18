nums = [5,1,23,31,12,4,9]

n = len(nums)

for i in range(n-2, -1, -1):
  is_swap = False
  for j in range(0, i+1):
    if nums[j] > nums[j+1]:
      nums[j], nums[j+1] = nums[j+1], nums[j]
      is_swap = True
  if is_swap == False:
    break

print(nums)


#Explanation: The outer loop iterates from the second last index to the first index. The inner loop compares adjacent elements and swaps them if they are in the wrong order. The is_swap flag is used to check if any swaps were made during the inner loop. If no swaps were made, it means the list is already sorted, and we can break out of the loop early for efficiency.

# In simple words, the bubble sort algorithm repeatedly compares adjacent elements and swaps them if they are in the wrong order. This process continues until the entire list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list with each iteration.

# Time complexity: O(n^2), Space complexity: O(1)