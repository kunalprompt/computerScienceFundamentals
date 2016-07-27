'''
Author - Kunal Sharma
Web - http://kunalprompt.github.io
'''
class BSTreeNode(object):
	"""BSTreeNode - Node of Binary Search Tree"""
	def __init__(self, data):
		super(BSTreeNode, self).__init__()
		self.data = data
		self.left = None
		self.right = None
	# getting data from a node
	def getData(self):
		return self.data
	# setting data for a node
	def setData(self, data):
		self.data = data
	# returning the left node of this node
	def getLeft(self):
		return self.left
	#returning the right node of this node
	def getRight(self):
		return self.right