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

  def add_to_head(self, value):
    # If no head / empty list:
    if self.head is None:
    # Create the new node with next = None
        new_node = Node(value, None)
    #  Set self.head = new node
        self.head = new_node
    # Set self.tail = new node
        self.tail = new_node
    # increment self.length
        self.length += 1
    else:
    # If head:
    # Create the new node
        new_node = Node(value, self.head)
    # New_node.next = self.head
    # Set self.head = new_node
        self.head = new_node
    # increment self.length
        self.length += 1
def remove_at_index(self, index):
    # Remove at index i:
    # 0) Check that length > i. If not, return None
    if index >= self.length:
        return None
    if self.length == 1 and index == 0:
        target = self.head
        self.head = None
        self.tail = None
        self.length = self.length - 1
        return target.value
    # Iterate through the loop i-1 times:
    prev_node = self.head
    for i in range(index - 1):
    # This will get us to prev_node points to the node before the target node
        prev_node = prev_node.next
    target = prev_node.next
    prev_node.next = target.next
    target.next = None
    self.length = self.length - 1
    return target.value