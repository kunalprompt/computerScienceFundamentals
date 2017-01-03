'''
Given n natural numbers. 
For t test cases, print sum of the numbers till the input x.

Example, 
n = 7
natural numbers = 0, 1, 2, 3, 4, 5, 6, 7

t = 2

when t = 1
x = 4
Output: 10

when t = 2
x = 5
Output: 15
'''

def main_without_dp_memoization():
	n = long(input())
	t = long(input())
	while t>0:
		x = long(input())
		s = 0
		for i in xrange(x+1):
			s += i
		print s
		t-=1


def main_with_dp_memoization():
	n = long(input())
	mem = [None]*(n+1)  # each index will contain sum upto that index
	mem[0] = 0
	t = long(input())
	while t>0:
		x = long(input())
		i = x - 1
		# find index upto which you have already calculated
		while(not mem[i] and i >0):
			i = i - 1
		i+=1
		while x>=i:
			mem[i] = i + mem[i-1]
			i+=1
		print mem[x]
		t-=1

if __name__ == "__main__":
	main_with_dp_memoization()
