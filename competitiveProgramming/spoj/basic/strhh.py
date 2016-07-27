def string(s):
	out_s = ""
	l = len(s)/2
	for i in range(0, l):
		if i%2==0:
			out_s += s[i]
	return out_s

def main():
	t = int(raw_input())
	while t:
		print string(raw_input())
		t-=1

if __name__=="__main__":
	main()
	# print string("your")
	# print string("progress")
	# print string("is")
	# print string("noticeable")
