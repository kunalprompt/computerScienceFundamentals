# http://www.spoj.com/problems/MUL/
n = int(raw_input())
while n:
	a, b = map(long, raw_input().split())
	print a*b
	n-=1
