
def findPower( x,n):
  #base case
  if n == 0:
      return 1
  
  a = findPower(x,n//2)
  if n%2==0:
      return a*a
  else:
      return a*a*x



def myPow( x: float, n: int) -> float:
  if n>=0:
      return findPower(x,n)
  else:
      return 1/findPower(x,n*(-1))

print(myPow(2.0, 10))  # Output: 1024.0

        