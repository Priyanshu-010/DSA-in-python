def printNumber(i, n):
  # base case
  if i > n:
    return
  # recursive case
  print(i, end=' ')
  printNumber(i+1, n)

printNumber(1, 10)


def fact(n):
  #base case
  if(n==0):
    return 1
  #recursive case
  return n * fact(n-1)

print(fact(5))

# Recursive stack: LIFO (Last In First Out) the last function call will be executed first and after that the second last function call will be executed and so on. The first function call will be executed at the end.
def fun(n):
  if n == 0:
    return
  fun(n-1)
  print(n, end=' ')

fun(5)

# Recuresive Tree: A recursive tree is a tree data structure that is defined recursively. Each node in the tree can have zero or more child nodes, and each child node can also have its own child nodes, forming a hierarchical structure. The base case of the recursion is typically when a node has no children, at which point the recursion stops.