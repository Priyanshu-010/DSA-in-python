# Leetcode 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return None

#         slow = head
#         fast = head
#         hasCycle = False

#         while fast and fast.next: # this is similar to fast != None or fast.next != None
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 hasCycle = True
#                 break
        
#         if not hasCycle:
#             return None
        
#         l = 0

#         while slow.next != fast:
#             slow = slow.next
#             l+=1
#         l+=1
#         slow = slow.next

#         slow = head
#         fast = head

#         for i in range(l):
#             fast = fast.next
        
#         while slow != fast:
#             fast = fast.next
#             slow = slow.next
        
#         return slow