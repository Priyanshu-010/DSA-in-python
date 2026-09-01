nums = [-1,0,3,5,9,12]
target = 9
n =len(nums)
low = 0
high= n-1

while low <= high:
  mid = (low+high)//2
  if nums[mid] == target:
    print(mid)
    break
  elif target > nums[mid]:
    low = mid+1
  elif target < nums[mid]:
    high = mid-1
  else:
    print(-1)

# Time Complexity: O(log n), Space complexity: O(1)


def bs(nums, low, high,x):
  if low > high:
    return -1
  
  mid = (low+high)//2
  if nums[mid] == x:
    return mid
  elif nums[mid] < x:
    return bs(nums,mid+1, high,x)
  else:
    return bs(nums,low, mid-1,x)


print(bs(nums,low,high,target))

# Time Complexity: O(log n), Space complexity: O(1)