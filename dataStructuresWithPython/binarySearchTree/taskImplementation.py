'''
Author - Kunal Sharma
Web - http://kunalprompt.github.io
'''

# importing modules
from bstNode import BSTreeNode
from bstMethods import *

# the root node of the tree
root=None

# taking the input from the user - list
l = map(int, raw_input("Enter the nodes data (Integers Only) seperated by spaces\n").split())
if len(l)>=1:
	root = BSTreeNode(l[0])
	for i in range(1, len(l)):
		node = BSTreeNode(l[i])
		insertNode(root, node)
	del l
	while(root):
		print "Follow the instructions below\nEnter 1 to Insert a Node\nEnter 2 to print Preorder, Inorder, and Postorder Traversals"
		print "Enter 3 to Search a node\nEnter 4 to delete a node\nEnter 5 to exit"
		t = int(raw_input())
		if t==1:
			try: data = int(raw_input())
			except: continue
			node = BSTreeNode(data)
			insertNode(root, node)
		elif t==2:
			traversal = []
			preorderTraversal(root, traversal)
			print "Pre-Order Traversal - ", traversal
			traversal = []
			inorderTraversal(root, traversal)
			print "In-Order Traversal - ", traversal
			traversal = []
			postorderTraversal(root, traversal)
			print "Post-Order Traversal - ", traversal
			del traversal
		elif t==3:
			try: data = int(raw_input())
			except: continue
			node = searchNode(root, data)
			if node is None: print "No such node exist in BSTree"
			else:
				print node
				print "Node Data - ", node.getData()
				print "Node Left - ", node.getLeft()
				print "Node Right - ", node.getRight()
		elif t==4:
			try: data = int(raw_input())
			except: continue
			root = deleteNode(root, data)
		else:
			deleteCompleteBSTree(root)
			print "Thanks!!!"
			exit(0)
	print "You've deleted the whole Binary Search Tree. Stay hungry to execute this code!"