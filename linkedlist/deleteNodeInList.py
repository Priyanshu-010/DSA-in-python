# Leetcode 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# code is just this much

# node.val = node.next.val
# node.next = node.next.next

# Explanation: 
# with an example: 
# How to become another person in the world? Two steps.
# Step One - change your appearance to whom you want to be.
# Step Two - kill that person.

# change the node to the next node
# kill the next node by changing the next of the current node to the next of the next node


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

def delete(node):
  node.val = node.next.val
  node.next = node.next.next

delete(node1) # You can provide any random node of the linked list but it should be a node that has a next node.

def print_linked_list(head):
  curr = head

  while curr!= None:
    print(curr.val, end=' ')
    curr = curr.next

print_linked_list(head)