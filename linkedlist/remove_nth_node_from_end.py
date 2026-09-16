# leetcode - 19 Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# This is the first approach where we take the length of the linked list and then we go to the kth position from the end and then we delete the next node of the kth node.

# curr = head
# l = 0

# while curr != None:
#   l += 1
#   curr = curr.next

# dummy = ListNode(0, head)
# curr = dummy
# k = l - n
# # curr = head
# for i in range(k):
#   curr = curr.next
# curr.next = curr.next.next

# return dummy.next


# Two pointers approach start the second pointer from nth node so that when the first pointer reaches the end the second pointer will be at the kth(which we want to remove) node from the end

# p1 = head
# p2 = head

# for i in range(n):
#   p2 = p2.next

# # edge case if n = len of linked list
# if p2 == None:
#   head = head.next
#   return head

# while p2.next != None:
#   p1 = p1.next
#   p2 = p2.next
# p1.next = p1.next.next

# return head
