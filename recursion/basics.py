def func(n):
  if n == 5:
    return
  print("Priyanshu")
  func(n+1)

func(1)

# Print x n times using recursion

def printX(x, n):
  if n == 0:
    return
  print(x, end=' ')
  printX(x, n-1)

printX("Priyanshu", 4)
print()

# 1 to n head recursion
def printNum(i, n):
  if i > n:
    return
  print(i, end=" ")
  printNum(i+1, n)
  
printNum(1,10)

print("Here the function ends")

# N to 1 using tail recursion

def printNto1(i, n):
  if i > n:
    return
  printNto1(i+1, n)
  print(i, end=" ")

printNto1(1, 5)

# N to 1 using head recursion

def printNto1H(n):
  if n == 0:
    return
  print(n)
  printNto1H(n-1)

printNto1H(5)

def sumOfN(sum, i, n):
  if i>n:
    print(sum)
    return
  sumOfN(sum+i, i+1, n)

sumOfN(0, 1, 4)

print("END")

# functional recursion: A function calls itself in the return statement of the function. The recursive call is the last statement to be executed in the function. This is also known as tail recursion.

def funcrec(n):
  if n == 1:
    return 1
  return n + funcrec(n-1)

print(funcrec(10))

# def printNumber(i, n):
#   # base case
#   if i > n:
#     return
#   # recursive case
#   print(i, end=' ')
#   printNumber(i+1, n)

# printNumber(1, 10)

print("Fact")
def fact(n):
  #base case
  if(n==0)or (n==1):
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