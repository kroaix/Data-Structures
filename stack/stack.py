"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# Using array as data structure for storage
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     # Adding to the bottom
#     # First in last out
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     # removing from the top
#     # First in last out
#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()
#         return

# Using LinkedList as data structure for storage
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    # Adding to the bottom
    # Last in first out
    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    # removing from the top
    # Last in first out
    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_head()