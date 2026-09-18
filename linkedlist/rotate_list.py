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

k = 2

if head== None or head.next == None:
  print(head)
l = 0
last = head
while last.next:
  last = last.next
  l+=1
l+=1

k = k%l
if k == 0:
  head

curr = head

for i in range(l-k-1):
  curr = curr.next

last.next = head
head = curr.next
curr.next = None


print(head.val)

def print_linked_list(head):
  curr = head

  while curr!= None:
    print(curr.val, end=' ')
    curr = curr.next

print_linked_list(head)
