def pattern(m, n):
	for i in range(m):
		row = ""
		for j in range(n):
			if i %2==0:
				if j%2==0:
					row+="*"
				else:
					row+="."
			else:
				if j%2==0:
					row+="."
				else:
					row+="*"
		print row

def main():
	t = int(raw_input())
	while t:
		m, n = map(int, raw_input().split())
		pattern(m, n)
		t-=1

if __name__=="__main__":
	main()
	# pattern(3, 1)
	# pattern(4, 4)
	# pattern(2, 5)