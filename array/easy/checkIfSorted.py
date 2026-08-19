nums = [3,4,5,6,7,8,9,10]

check= "sorted"

for i in range(1, len(nums)):
  if nums[i]<nums[i-1]:
    check = "not sorted"

print(check)