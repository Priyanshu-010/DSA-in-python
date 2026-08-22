nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10] 

n = len(nums1)
m = len(nums2)
i =0
j=0
result = []

while i< n and j<m:
  if nums1[i] < nums2[j]:
    if len(result) ==0 or result[-1] != nums1[i]:
      result.append(nums1[i])
    i+=1
  else:
    if len(result) ==0 or result[-1] != nums1[j]:
      result.append(nums2[j])
    j+=1

while i<n:
  if len(result) ==0 or result[-1] != nums1[i]:
    result.append(nums1[i])
  i+=1

while j<m:
  if len(result) ==0 or result[-1] != nums2[j]:
    result.append(nums2[j])
  j+=1

print(result)

# Time Complexity O(n+m), Space Complexity O(n+m)

# Code explanation: 

# The while loop iterates over the elements of nums1 and nums2, comparing them in pairs.

# If nums1[i] is less than nums2[j], it appends nums1[i] to the result if it's not already present. It then increments i to move to the next element in nums1.

# If nums1[i] is greater than or equal to nums2[j], it appends nums2[j] to the result if it's not already present. It then increments j to move to the next element in nums2.

# The while loops continue until both i and j reach the end of their respective arrays.

# Finally, it appends any remaining elements in nums1 to the result and any remaining elements in nums2 to the result.