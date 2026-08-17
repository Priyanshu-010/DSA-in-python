nums = [4,1,7,6,3,2,8]

n = len(nums) -1

def partition(nums, low, high):
  pivot = nums[low]
  i, j = low, high   
  while i<j:
    while nums[i]<= pivot and i<=high-1:
      i+=1
    while nums[j]> pivot and j>=low+1:
      j-=1

    if i<j:
      nums[i], nums[j] = nums[j], nums[i]

  nums[low], nums[j] = nums[j], nums[low]
  return j

def quick_sort(nums, low, high):
  if low<high:
    p_index = partition(nums, low, high)
    quick_sort(nums, low, p_index-1)
    quick_sort(nums, p_index+1, high)

quick_sort(nums, 0, n)
print(nums)

# Explanation: The quick_sort function recursively sorts the input list by selecting a pivot element and partitioning the list into two halves based on the pivot. The partition function rearranges the elements such that all elements less than or equal to the pivot are on the left side, and all elements greater than the pivot are on the right side. The process is repeated for each half until the entire list is sorted.

# In simple words, the quick sort algorithm selects a pivot element and partitions the list into two halves based on the pivot. It then recursively sorts each half until the entire list is sorted.