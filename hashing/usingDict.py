n = [5,6,3,1,1,4,5,10,9,9,7]
m = [10,111,321,4,25,5,7,21]

dict={}
max = 0
elem = 0
for i in n:
  dict[i] = dict.get(i, 0)+1

for k in dict:
  if dict[k]>max:
    max = dict[k]
    elem = k
print(max)
print(elem)

for j in m:
  if j<0 or j>10:
    print(0, end=" ")
  else:
    print(dict.get(j,0), end=" ") # Why we used 0 because if the key is not present in the dictionary, it will return 0 instead of throwing an error. This way, we can safely get the count of occurrences for each element in list m without worrying about missing keys.

# What we did in this code is we created a dictionary to count the occurrences of each element in list n. Then, we found the element with the maximum occurrences and printed it. Finally, we iterated through list m and printed the count of each element based on the dictionary we created, handling cases where the element is not present in the dictionary by returning 0.



