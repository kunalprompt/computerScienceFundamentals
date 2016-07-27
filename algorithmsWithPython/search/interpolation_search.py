def interpolation_search(array, bottom, top, item):
	while(bottom<=top):
		mid = bottom + (top-bottom)*((item - array[bottom])/(array[top]-array[bottom]))
		# print mid
		try:
			if item==array[mid]:
				return mid
		except:
			return -1
		if item<array[mid]:
			top = mid-1
		else:
			bottom = mid+1
	return -1

if __name__=="__main__":
	print interpolation_search([1, 2, 3, 4, 5, 6], 0, 5, 2)