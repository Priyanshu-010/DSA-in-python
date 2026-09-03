nums = [-1,0,3,5,9,12]
target = 1

n = len(nums)
low = 0
high = n-1
lb = n

while low <= high:
  mid = (low+high)//2
  if nums[mid] >=target:
    lb = mid
    high = mid -1
  else:
    low = mid+1

print(lb)

# Time Complexity: O(log n), Space complexity: O(1)