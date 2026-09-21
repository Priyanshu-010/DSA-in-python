# Leetcode 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Code:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None or head.next == None:
#             return False

#         slow = head
#         fast = head

#         while fast and fast.next: # this is similar to fast != None or fast.next != None
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True
        
#         return False

# In this code we are checking if the linked list has a cycle or not
# Explanation:
# We are using the fast and slow pointer approach
# Fast pointer travels two times and slow pointer travels one time
# 1. If the linked list has a cycle, then the fast pointer will reach the slow pointer
# 2. If the linked list does not have a cycle, then the fast pointer will reach the end of the linked list