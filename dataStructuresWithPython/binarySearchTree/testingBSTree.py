'''
Author - Kunal Sharma
Web - http://kunalprompt.github.io
'''
# Automating testing of any tree to be a BST

# importing modules
from bstNode import BSTreeNode
from bstMethods import *

# code testing - automated
# initializing the tree and testing insertNode() method
def initializeBSTree(list_items):
	assert len(list_items)>=1, "No list items" 
	root = BSTreeNode(l[0])
	for i in range(1, len(list_items)):
		node = BSTreeNode(l[i])
		insertNode(root, node)
	return root

# check whether tree created is BST or not
def isBSTree(root, minimum, maximum):
	if root is None:
		return 1
	if root.getData()<=minimum or root.getData()>=maximum:
		return 0
	result = isBSTree(root.getLeft(), minimum, root.getData())
	result = result and isBSTree(root.getRight(), root.getData(), maximum)
	return result

l = map(int, raw_input().split())
root = initializeBSTree(l)

minimum = float("-infinity")
maximum = float("infinity")
if isBSTree(root, minimum, maximum): print True 
else: print False
