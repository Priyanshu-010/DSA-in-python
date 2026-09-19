# Leetcode 160 - Intersection of Two linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/



# I am just pasting the solutions

# Length of both LL appraoach

# l1 = 0
# currA = headA
# while currA:
#   l1+=1
#   currA = currA.next
# l2 = 0
# currB = headB
# while currB:
#   l2+=1
#   currB = currB.next

# # maxi = max(l1,l2)
# # mini = min(l1,l2)
# # diff = maxi - mini

# if l1 > l2:
#   for _ in range(l1 - l2):
#     headA = headA.next
# elif l2 > l1:
#   for _ in range(l2 - l1):
#     headB = headB.next

# while headA and headB:
#   if headA == headB:
#     return headA
#   headA = headA.next
#   headB = headB.next
# return None

# Two pointers approach

# p1 = headA
# p2 = headB

# c = 0
# while True:
#   if p1 == p2:
#     return p1
#   p1 = p1.next
#   p2 = p2.next

#   if p2==None:
#     c+=1
#     p2= headA
#   if p1== None:
#     p1 = headB

#   if c>1:
#     return None