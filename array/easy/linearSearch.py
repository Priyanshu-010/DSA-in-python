nums = [5,3,9,8,1,6,4,-10,-100]
target = 9

for i in range(0,len(nums)):
  if nums[i] == target:
    print(i)
    break
print("Not found")

# Time Complexity: O(n), Space complexity: O(1)