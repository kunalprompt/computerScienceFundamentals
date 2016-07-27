# Basics of Binary Tree
# creating a BinaryTree Node
class BinaryTreeNode():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	def setData(data):
		self.data = data
	def getData(self):
		return self.data
	def getLeft(self):
		return self.left
	def getRight(self):
		return self.right

# creating root node
root = BinaryTreeNode(1)
print root.getData()
print root.getLeft()
print root.getRight()

# adding a node to root
n = BinaryTreeNode(2)
root.left = n
print root.getLeft()
print n.getData()
print n.getLeft()
print n.getRight()