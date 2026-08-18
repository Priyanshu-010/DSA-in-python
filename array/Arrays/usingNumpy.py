from numpy import *

val = array([1, 2, 3, 4, 5])

lin = linspace(10, 20, 5) # creating an array of 5 elements from 10 to 20.

arr = arange(1, 15, 2) # creating an array of elements from 1 to 15 with a step of 2.

log = logspace(1, 40, 5) # creating an array of 5 elements from 10^1 to 10^40.

zero = zeros(5) # creating an array of 5 elements with all values as 0.

one = ones(5) # creating an array of 5 elements with all values as 1.

sameValues = full(5, 7) # creating an array of 5 elements with all values as 7.

print(log)
print(zero)
print(one)
print(sameValues)

for x in val:
  print(x, end=" ")

print("\n")

for x in lin:
  print(x, end=" ")

print("\n")

for x in arr:
  print(x, end=" ")