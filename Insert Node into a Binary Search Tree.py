#!/bin/python3

import math
import os
import random
import re
import sys

class BstNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#
# Complete the 'insert_into_binary_tree' function below.
#
# The function is expected to return a BstNode, the root node of the tree after insertion.
# The function accepts BstNode bst, the root of the binary search tree, if none, return the new root node.
# The function accepts INTEGER value as the value to insert. 

def insert_into_binary_tree(bst, value):
    # implement insert here
    # if the root is None, create a new node and return it
    if bst is None:
        return BstNode(value)
 
    # if the given key is less than the root node,
    # recur for the left subtree
    if key < bst.data:
        bst.left = insert(bst.left, value)
 
    # otherwise, recur for the right subtree
    else:
        # key >= root.data
        bst.right = insert(bst.right, value)
 
    return bst


if __name__ == '__main__':

    input_numbers = []

    input_numbers_count = int(input().strip())
    for _ in range(input_numbers_count):
        input_numbers_item = int(input().strip())
        input_numbers.append(input_numbers_item)
        
    bst = None
    for input_number in input_numbers:
        bst = insert_into_binary_tree(bst, input_number)
        
    def print_helper(bst):
        if not bst:
            return
        print_helper(bst.left)
        print(bst.value)
        print_helper(bst.right)
    print_helper(bst)
    
        