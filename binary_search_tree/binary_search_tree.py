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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    # compare value of node to parent node and decides whether to insert to left or right side of the binary tree
    def insert(self, value):
        # compare new value with parent node
        # if the new value is less than the parent value
        if value <= self.value:
            # if empty construct a node based on the value we are given
            if self.left is None:
                self.left = BSTNode(value)
            # otherwise, insert left
            else:
                self.left.insert(value)
        # same written above goes for right
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
            #if target is more than or equal to value - go right
        elif target >= self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return True

        # while self.value != target:
        #     #if target is less than value and left is not empty
        #     if target < self.value and self.left is not None:
        #         self = self.left
        #     elif target > self.value and self.right is not None:
        #         self = self.right
        #     else:
        #         return False
        # else:
        #     return True

    # Return the maximum value found in the tree
    def get_max(self):
        # checking right because right is always bigger than left - we do not care about the left
        while self.right is not None:
            self = self.right
        return self.value

    # Part 2 -----------------------

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
