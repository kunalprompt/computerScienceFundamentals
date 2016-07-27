# creating a Binary Tree Node
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

# creating a binary Binary Tree - level 0
root = BinaryTreeNode(1)

# creating node at level 1
root.insertLeft(2)
root.insertRight(3)

# creating node at level 2
root.left.insertLeft(4)
root.left.insertRight(5)
root.right.insertLeft(6)
root.right.insertRight(7)

# making a function for pre-order traversal
def inorderTraversal(root, result):
	if not root:
		return
	else:
		inorderTraversal(root.left, result)
		result.append(root.getData())
		inorderTraversal(root.right, result)

result = []
inorderTraversal(root, result)
print result