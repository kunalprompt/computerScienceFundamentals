# http://www.spoj.com/problems/FCTRL2/
def factorial(n):
	output = 1
	for i in range(2, n+1):
		output = output*i
	return output

t = int(raw_input())
while(t):
	f = int(raw_input())
	print factorial(f)
	t-=1
