nums = [55, 32, -97, 99, 3, 67]

largest = nums[0] #float("-inf")  for +ve float("inf") easy way max(nums) 
n = len(nums)

for i in range(n):
  if nums[i] > largest:
    largest = nums[i]

print(largest)