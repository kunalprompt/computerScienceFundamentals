# creating a linkedlist node
class LinkedListNode():
	def __init__(self, data):
		self.data = data
		self.next = None
# creating a method for reversing a linked list
def reverseLL(root):
	ptr = root
	previous = None
	while (ptr!=None):
		current = ptr
		nextNode = ptr.next
		current.next = previous
		ptr = nextNode
		previous = current
	return previous

# creating a linked list
head = LinkedListNode(3)
node1 = LinkedListNode(2)
head.next = node1
node1.next = LinkedListNode(5)

# traversing the linked list
print "LinkedList - "
temp = head
while(temp != None):
	print temp.data,
	temp = temp.next

# reverse the linked list
print "\nReversed LinkedList - "
tempHead = reverseLL(head)
temp = tempHead
while(temp != None):
	print temp.data,
	temp = temp.next