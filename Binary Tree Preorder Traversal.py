#!/bin/python3

import math
import os
import random
import re
import sys

class BinarySearchTreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None

def insert_node_into_binary_search_tree(node, node_data):
    if node == None:
        node = BinarySearchTreeNode(node_data)
    else:
        if (node_data <= node.data):
            node.left = insert_node_into_binary_search_tree(node.left, node_data)
        else:
            node.right = insert_node_into_binary_search_tree(node.right, node_data)

    return node

def print_binary_search_tree_inorder_traversal(node, sep):
    if node == None:
        return

    print_binary_search_tree_inorder_traversal(node.left, sep)

    if node.left:
        print(sep, end='')
    print(node.data, end='')

    if node.right:
        print(sep, end='')

    print_binary_search_tree_inorder_traversal(node.right, sep)

#
# Complete the 'preorder_traversal' function below.
#
# The function accepts INTEGER_BINARY_SEARCH_TREE bst as parameter.
#

#
# For your reference:
#
# BinarySearchTreeNode:
#     int data
#     BinarySearchTreeNode left
#     BinarySearchTreeNode right
#
#

def preorder_traversal(bst):
    # Write your code here
    print (bst.data)
    if bst.left is not None:
        preorder_traversal(bst.left)
    if bst.right is not None:
        preorder_traversal(bst.right)
        
        

if __name__ == '__main__':
    input_bst_count = int(input().strip())

    input_bst = None

    for _ in range(input_bst_count):
        input_bst_item = int(input().strip())
        input_bst = insert_node_into_binary_search_tree(input_bst, input_bst_item)

    preorder_traversal(input_bst)
