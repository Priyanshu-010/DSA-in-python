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
