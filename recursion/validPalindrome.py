s = "nitin"

# With Recursion

def isPalindrome(s, l, r):
  if l>=r:
    return True
  if s[l] != s[r]:
    return False

  return isPalindrome(s, l+1, r-1)
  

print(isPalindrome(s, 0, len(s)-1))



# With loop

def withLopp(s):
  l = 0
  r = len(s)-1
  while l<r:
    if s[l] != s[r]:
      return False
    l +=1
    r -=1

  return True

print(withLopp(s))

# Time complexity: O(n/2) ~ O(n), Space complexity: O(1)