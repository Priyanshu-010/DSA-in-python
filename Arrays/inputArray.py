from array import *

# Taking input from the user to create an array of integers.

# arr = array('i', []) # creating an empty array of integers

# n = int(input("Enter the number of elements you want to add in the array: "))

# for i in range(0, n):
#   arr.append(int(input("Enter the element: ")))

# for x in arr:
#   print(x, end=" ")


# -----------------------------------------------------------------------------

# Finding the index of an element in the array.
arr = array('i', [12, 23, 34, 45, 56, 67, 78, 89, 90]) # creating an integers array

i = arr.index(45) # finding the index of the element 45 in the array.

print(i)

