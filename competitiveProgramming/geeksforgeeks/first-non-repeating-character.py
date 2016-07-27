"""
Given a string s = "GeeksforGeeks", print the first non repeating character of this string.
Output: f

The same question can be extended to find kth non repeating character.
"""

def firstNonRepeatingCharacter(s):
	h = {}
	for i in s:
		if i in h:
			h[i]+=1
		else:
			h[i] = 1
	index = 0  # for non repeating character
	for i in s:
		if h[i]==1:
			index += 1
			if index==2:  # for 2nd non repeating character
				return i, h[i]

def main():
	t = int(raw_input())
	while t:
		print firstNonRepeatingCharacter(raw_input())
		t-=1

if __name__ == '__main__':
	main()
	# print firstNonRepeatingCharacter("GeeksforGeeks")
	# print firstNonRepeatingCharacter("kunal sharma")
