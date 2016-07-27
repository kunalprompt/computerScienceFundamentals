# binary search with python
# binary search requires a sorted list only
def binarySearch(list, target):
	low = 0
	high = len(list)-1
	while low <= high:
		mid = int((low+high)/2)
		if list[mid]==target:
			return mid
		elif target<list[mid]:
			high = mid-1
		elif target>list[mid]:
			low = mid+1
	return None

l = [1, 2, 3, 4, 5]
l = sorted(l)
print l
result = binarySearch(l, 1)
print "Target found at index -", result