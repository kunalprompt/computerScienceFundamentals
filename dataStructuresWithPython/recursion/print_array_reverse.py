def printArrayReverse(arr):
	if not arr:
		return
	printArrayReverse(arr[1:])
	print arr[0],

printArrayReverse([1, 2, 3, 4, 5])
