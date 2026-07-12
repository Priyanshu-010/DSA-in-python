import array
# import array as arr
# we can give name to the array module as arr and then we can use arr instead of array.
from array import *
# or we can use this to import all the functions and classes from the array module.

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # creating an array of integers
# print(val)

# Printing the elements of the array using for loop

# for i in range(0,5):
#   print(val[i], end=" ")

# print("\n")

# for x in val:
#   print(x, end=", ")

# print("\n")

# methods of array module

# print(val.typecode)
# val.reverse()

# for i in val:
#   print(i, end=" ")


# val.insert(1, 50)
# val.append(60)
# val[2] = 100

# copyArray = array(val.typecode, (x*2 for x in val))

# copyArray.pop()
# copyArray.remove(100) to remove a specific value from the array.


abc = val[2:5] # slicing the array from index 2 to 5 (5 is exclusive)
#abc = val[2:-3] # this will not include the last 3 elements of the array.
# abc = val[::-1] # this will reverse the array


for i in abc:
  print(i, end=" ")


print("\n")