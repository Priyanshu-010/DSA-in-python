# leetcode 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

node1 = Node(5)
node2 = Node(7)
node3 = Node(3)
node4 = Node(1)
node5 = Node(2)
node6 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

curr = head
l = 0
while curr!= None:
    curr = curr.next
    l += 1

curr = head
newL = l//2

for i in range(newL):
    curr = curr.next


def print_linked_list(head):
  curr = head

  while curr!= None:
    print(curr.val, end=' ')
    curr = curr.next

print_linked_list(curr)

# Time complexity: O(n), Space complexity: O(1)

print()

# Very IMPORTANT
# Fast and slow pointer approach

def fast_slow(head):
  fast = head
  slow = head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
  
  return slow

print_linked_list(fast_slow(head))

# explanation: fast pointer travels two times and slow travels one time so when fast pointer reaches the end slow pointer is in the middle
   