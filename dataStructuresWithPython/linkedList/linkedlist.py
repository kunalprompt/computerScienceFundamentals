from random import randint

class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def getNext(self):
		return self.next

	def getData(self):
		return self.data

	def setNext(self, node):
		self.next = node

def get_length(root):
	count = 0
	while root:
		count+=1
		root = root.getNext()
	return count

def print_list_iterate(root):
	while root:
		print root.getData(), "-->",
		root = root.getNext()

def print_list_recurse(root):
	if root is None:
		return
	print root.getData(), "-->",
	print_list_recurse(root.getNext())

def print_reverse_recurse(root):
	if root is None:
		return
	print_reverse_recurse(root.getNext())
	print root.getData(), "-->",

def main():
	root1 = Node(12)
	count = 0
	prev = root1
	while(count<5):
		node = Node(randint(20, 300))
		prev.setNext(node)
		prev = node
		del node
		count+=1

	print 'Linked List:'
	print print_list_recurse(root1)
	print 'Length of Linked List:'
	print get_length(root1)
	print 'Reverse of Linked List:'
	print print_reverse_recurse(root1)

main()
