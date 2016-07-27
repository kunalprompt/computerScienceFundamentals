def pattern(m, n):
	for i in range(m):
		row = ""			
		for j in range(n):
			if i==0 or i==m-1:
				row += "*"
			elif j==0 or j==n-1:
				row += "*"
			else:
				row += "."
		print row

def main():
	t = int(raw_input())
	while t:
		m, n = map(int, raw_input().split())
		pattern(m, n)
		t-=1

if __name__=="__main__":
	# main()
	pattern(1, 3)
	# pattern(3, 1)
	# pattern(4, 8)
	# pattern(2, 5)
	# pattern(3, 5)