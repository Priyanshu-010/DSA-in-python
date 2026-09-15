class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

node1 = Node(5)
node2 = Node(7)
node3 = Node(3)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

# print(head.val)
# print(node2.val)
# print(node1.next.next.val)

# traverse a linked list
def print_linked_list(head):
  curr = head

  while curr!= None:
    print(curr.val, end=' ')
    curr = curr.next

# ================================================================================

# insertion at the beginning

# newNode= Node(4)

# newNode.next= head
# head = newNode

# print_linked_list(head)

# ================================================================================

# insertion at end

# lastNode = Node(8)

# curr = head

# while curr.next != None:
#   curr = curr.next

# curr.next = lastNode


# print_linked_list(head)


#===============================================================================

# Insertion at Kth index

# k = 2

# curr = head
# for i in range(k-1):
#   curr = curr.next

# newNode = Node(4)
# newNode.next = curr.next
# curr.next = newNode

# print_linked_list(head)

# explanation of the code:
# new node ke next ko curr ke next pe point kardo or curr ke next ka new node ko point kardo is se newNode desired index pe insert hojayega

# ================================================================================

# delete the first Node

# head = head.next
# print_linked_list(head)

# ================================================================================

# delete the last Node

# curr = head

# while curr.next.next !=None:
#   curr = curr.next

# curr.next = None

# print_linked_list(head)

# ================================================================================

# delete the Kth Node

k = 2

curr = head
for i in range(k-1):
  curr = curr.next
newNode = Node(4)

curr.next = curr.next.next

print_linked_list(head)