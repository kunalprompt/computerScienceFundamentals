# Add new methods to the Binary Tree Node

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
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTreeNode(newNode)
		else:
			temp = BinaryTreeNode(newNode)
			temp.left = self.left
			self.left = temp
	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTreeNode(newNode)
		else:
			temp = BinaryTreeNode()
			temp.right = self.right
			self.right = temp

root = BinaryTreeNode(1)
root.insertLeft(2)
root.insertRight(3)
print root.getLeft().getData()
root.left.insertLeft(4)
print root.left.left.getData()