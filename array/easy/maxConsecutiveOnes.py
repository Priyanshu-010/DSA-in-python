nums = [1,1,0,1,1,1]

n= len(nums)

count = 0
max_count = 0

for i in range(0, n):
  if nums[i] ==1:
    count +=1

  else:
    max_count = max(count, max_count)
    count = 0

print(max(max_count, count))

# Time Complexity: O(n), Space complexity: O(1)

# Explanation of this code: 

# We initialize two variables count and max_count to keep track of the current count of consecutive ones and the maximum count of consecutive ones, respectively.

# We iterate through the input list nums using a for loop.

# If the current element nums[i] is 1, we increment the count by 1.

# If the current element nums[i] is 0, we update the max_count to the maximum of the current count and the previous max_count, and reset the count to 0.

# After the loop, we print the maximum count of consecutive ones, which is the maximum of the current count and the previous max_count.