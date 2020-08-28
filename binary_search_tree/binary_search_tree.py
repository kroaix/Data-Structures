"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare target value to node value
        #if value >= node.value
        if value >= self.value:
            #go right
            #if node.right is none
            if self.right is None:
                #create new node there
                self.right = BSTNode(value)
            else: #self.right is a BSTNode
                #do the same thing (recurse)
                #insert value into node.right
                #right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)

        #else if value < node.value
        if value < self.value:
            #go left
            #if node.left is none
            if self.left is None:
                #create node
                self.left = BSTNode(value)
            else:
                #do the same thing
                #compare and go left or right
                #insert value into node.left
                left_child = self.left
                left_child.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Compare target value to node.value
        # If target == node.value:
        if target == self.value:
        # return True
            return True

        # If target > node.value:
        if target > self.value:
        # Go right
        # If node.right is None:
        # We've traversed the tree and haven't found it
        # return False    
            if self.right is None:
                return False
            else:
            # return node.right.contains(target)
                return self.right.contains(target)

        # Else if target < node.value
        if target < self.value:
        # Go Left
        # If node.left is None:
        # return False
            if self.left is None:
                return False
        # Else:
            else:
        # Do the same thing
        # (compare, go left or right)
        # return node.left.contains(target)
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # the node with the maximum value will also be the right-most node
        #recursive
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

        #iterative
        # while self.right is not None:
        #     self = self.right
        
        # return self.value



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Will have to look at both branches
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            node.left.in_order_print(node.left)
            print(node.value)
        else:
            print(node.value)
        
        if node.right is not None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Start at the root
        queue = Queue()
        # Push it onto the queue
        queue.enqueue(node)
        # While queue is not empty:
        while len(queue) > 0:
        # Cur_node = Remove from the queue
            cur_node = queue.dequeue()
        # Add cur_node children to the queue
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right) 
        # Process cur_node
            print(cur_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Start at the root
        stack = Stack()
        # Push it onto the stack
        stack.push(node)
        # While stack is not empty:
        while len(stack) > 0:
        # Cur_node = Remove from stack
            cur_node = stack.pop()
        # Add cur_node children to the stack
            if cur_node.left:
                stack.push(cur_node.left)
            if cur_node.right:
                stack.push(cur_node.right)
        # Process cur_node
            print(cur_node.value)
            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
