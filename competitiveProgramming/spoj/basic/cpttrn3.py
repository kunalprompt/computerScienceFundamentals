def pattern(r, c):
	for i in range(0, r*3+1):
		out = ""
		if i%3==0:
			row_flag = True
		else:
			row_flag = False
		for j in range(0, c*3+1):
			if row_flag:
				out+="*"
			else:
				if j%3==0:
					out+="*"
				else:
					out+="."
		print out

def main():
	t = int(raw_input())
	while t:
		m, n = map(int, raw_input().split())
		pattern(m, n)
		t-=1

if __name__ == '__main__':
	main()
	# pattern(3, 1)
	# pattern(4, 4)
	# pattern(2, 5)