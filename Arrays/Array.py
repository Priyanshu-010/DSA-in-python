import array
# import array as arr
# we can give name to the array module as arr and then we can use arr instead of array.
from array import *
# or we can use this to import all the functions and classes from the array module.

val = array.array('i', [1, 2, 3, 4, 5])
# print(val)

for i in range(0,5):
  print(val[i], end=" ")

print("\n")

for x in val:
  print(x, end=", ")