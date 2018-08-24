# Given two binary trees, write a function 
# to check if they are equal or not.

# Two binary trees are considered equal if they are 
# structurally identical and the nodes have the same value. 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
    	if p == None and q != None:
    		return False
    	elif p != None and q == None:
    		return False
    	elif p == None and q == None:
    		return True  # missed this at the first submission
    	else:
    		if p.val != q.val:
    			return False
    		else:
    			if self.isSameTree(p.left,q.left) == False:
    				return False
    			if self.isSameTree(p.right,q.right) == False:
    				return False
    			return True










        