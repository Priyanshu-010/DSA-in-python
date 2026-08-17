nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
      # 0 ,1, 2, 3, 4, 5, 6, 7, 8

def merge_array(left, right):
  result = []
  i = j = 0
  n, m = len(left), len(right)

  while i<n and j<m:
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  if i < n:
    result.extend(left[i:])
  if j< m:
    result.extend(right[j:])

  return result

  # Or while loop method

  # if i < n:
  #   while i < n:
  #     result.append(left[i])
  #     i += 1

  # if j < m:
  #   while j < m:
  #     result.append(right[j])
  #     j += 1

  # return result

def merge_sort(nums):
  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  return merge_array(left, right)


print(merge_sort(nums))