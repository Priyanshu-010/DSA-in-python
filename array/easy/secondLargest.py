nums = [55, 32, -97, 99, 3, 67]

largest = float("-inf")  # for +ve float("inf") easy way max(nums) 
secondLargest = float("-inf")
n = len(nums)

for i in range(n):
  largest = max(largest, nums[i])

for i in range(n):
  if nums[i]>secondLargest and nums[i] != largest:
    secondLargest = nums[i]


# for i in range(n):
#   if nums[i]> largest:
#     secondLargest = largest
#     largest = nums[i]
#   elif nums[i] > secondLargest and nums[i] != largest:
#     secondLargest = nums[i]

print(secondLargest)