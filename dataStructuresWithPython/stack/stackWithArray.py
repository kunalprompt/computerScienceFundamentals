class Stack():
	def __init__(self, limit=5):
		self.stk = []
		self.limit=limit
	def push(self, data):
		self.stk.append(data)
	def pop(self):
		return self.stk.pop()
	def isEmpty(self):
		return len(self.stk)==0
	def isFull(self):
		return len(self.stk)==5
	def Top(self):
		return self.stk[len(self.stk)-1]
	def Size(self):
		return len(self.stk)
s = Stack()
print s.isEmpty()
s.push(10)
s.push(2)
s.push(3)
s.push(4)
s.push(1)
print s.isFull()
print s.pop()
print s.pop()
print s.pop()
print s.isEmpty()
print s.Top()
s.push(1)
print s.Top()
print s.Size()