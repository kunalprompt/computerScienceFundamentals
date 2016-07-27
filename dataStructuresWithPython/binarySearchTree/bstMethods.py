'''
Author - Kunal Sharma
Web - http://kunalprompt.github.io
'''
# insertion into binary search tree
def insertNode(root, node):
	if root is None:
		root = node
	else:
		if root.getData() > node.getData():
			if root.getLeft() is None:
				root.left = node
			else:
				insertNode(root.getLeft(), node)
		else:
			if root.getRight() is None:
				root.right = node
			else:
				insertNode(root.getRight(), node)

# searching a node in the binary search tree - returns the first matching node
def searchNode(root, data):
	thisNode = root
	while thisNode:
		if data==thisNode.getData():
			return thisNode
		elif data<thisNode.getData():
			thisNode = thisNode.getLeft()
		else:
			thisNode = thisNode.getRight()
	return None

# pre-order traversal
def preorderTraversal(root, traversedValues):
	if root is None: return
	traversedValues.append(root.getData())
	preorderTraversal(root.getLeft(), traversedValues)
	preorderTraversal(root.getRight(), traversedValues)

# in-order traversal
def inorderTraversal(root, traversedValues):
	if root is None: return
	inorderTraversal(root.getLeft(), traversedValues)
	traversedValues.append(root.getData())
	inorderTraversal(root.getRight(), traversedValues)

# post-order traversal
def postorderTraversal(root, traversedValues):
	if root is None: return
	postorderTraversal(root.getLeft(), traversedValues)
	postorderTraversal(root.getRight(), traversedValues)
	traversedValues.append(root.getData())

# deleting a node from Binary Search tree - new root is returned from this method
def deleteNode(root, data):
	# if the node to be deleted is root
	if root.getData()==data:
		if root.getLeft() and root.getRight():
			[parentNode, successorNode] = findMinimum(root.getRight(), root)
			if parentNode.getLeft() == successorNode:
				parentNode.left = successorNode.getRight()
			else:
				parentNode.right = successorNode.getRight()
			successorNode.left = root.left
			successorNode.right = root.right
			return successorNode
		else:
			if root.getLeft():
				return root.getLeft()
			else:
				return root.getRight()
	else:
		if root.getData() > data:
			if root.getLeft():
				root.left = deleteNode(root.left, data)
		else:
			if root.getRight():
				root.right = deleteNode(root.right, data)
	return root

# to find the minimum of current subtree
def findMinimum(root, parent):
	if root.getLeft():
		return findMinimum(root.getLeft(), root)
	else:
		return [parent, root]

# deleting complete BSTree
def deleteCompleteBSTree(node):
    if node:
        # recurse: visit all nodes in the two subtrees
        deleteCompleteBSTree(node.left)           
        deleteCompleteBSTree(node.right)
        node.left = None
        node.right = None