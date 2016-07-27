# linear search with python
def linearSearch(list, target):
	for i in range(len(list)):
		if list[i]==target:
			return i
	return None

l = [1, 2, 3, 4, 43, 23]
print l
result = linearSearch(l, 23)
print "Target found at index -", result