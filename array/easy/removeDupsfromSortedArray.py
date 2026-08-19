nums = [1,1,1,2,3,4,4,7,9,9,9,10]
n= len(nums)

freq= {}
for i in range(0,n):
  freq[nums[i]] = 0

j = 0
for k in freq:
  nums[j] = k
  j+=1

print(nums)
print(len(freq))