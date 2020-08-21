class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def __str__(self):
    pass

  def add_to_tail(self, value):
    #check if there's a tail
    #if there is no tail (empty list)
    if self.tail is None: #could also check length if tail = None
      #create a new node
      new_tail = Node(value, None)
      #set self.head and self.tail to the new node
      self.head = new_tail
      self.tail = new_tail
    #if there is a tail (general case)
    else:
      #create a new node with the value we want to add next = None
      new_tail = Node(value, None)
      #set current tail.next to the new node
      old_tail = self.tail
      old_tail.next = new_tail
      #set self.tail to the new node
      self.tail = new_tail
      #increment length
    self.length += 1

  def remove_head(self):
    #if no head (empty list)
    if self.head is None:
      return None
    #list with one element
    if self.head == self.tail:
      #set self.head to current_head.next (which is also None)
      current_head = self.head
      self.head = None
      #set self.tail to None
      self.tail = None
      #decrement length
      self.length -= 1
      return current_head.value
    #if head (General case)
    else:
      #set self.head to current_head.next
      current_head = self.head
      self.head = current_head.next
      #decrement length
      self.length -= 1
      return current_head.value

  def remove_tail(self):
    # Remove Tail:
    # Check if it's there
    if self.tail is None:
      return None

    # List of 1 element:
    elif self.head == self.tail:
      # Save the current_tail.value
      current_tail = self.tail
      # Set self.tail to None
      self.tail = None
      # Set self.head to None
      self.head = None
      self.length -= 1
      return current_tail.value

    # General case:  
    else:     
    # Start at head and iterate to the next-to-last node
      current_node = self.head
    # Stop when current_node.next == self.tail
      while current_node.next is not self.tail:
        # keep iterating
        current_node = current_node.next
    # Save the current_tail value
      current_tail = self.tail
    # Set self.tail to current_node
      self.tail = current_node
    # Set current_node.next to None
      current_node.next = None
      self.length -= 1
      return current_tail.value