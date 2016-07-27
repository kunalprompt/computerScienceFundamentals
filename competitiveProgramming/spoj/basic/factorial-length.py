# http://www.spoj.com/problems/LENGFACT/
from math import log10, sqrt

# usind striling's factoial approximation

SQRT_2_PI = 2.5066
E = 2.7182

def striling_factorial_length(n):
	global SQRT_2_PI, E
	return long(log10(SQRT_2_PI*sqrt(n)*pow(n/E, n))) + 1

def factorial_length(n):
	output = 1
	for i in range(2, n+1):
		output *= i
	return long(log10(output))+1

t = int(raw_input())
while(t):
	print striling_factorial_length(long(raw_input()))
	t-=1
