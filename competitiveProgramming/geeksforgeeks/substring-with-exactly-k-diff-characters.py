"""
Count number of substring with exactly k distinct characters.
Input: abc, k=2
Output: 2 
{"ab", "bc"}

Input: aba, k=2
Output: 3
{"ab", "aba", "ba"}
"""

def countExactlyKSubstrings(s, k):
	indexes = []
	count = 0
	i = 0
	j = 0
	while i<len(s):
		h = []
		h.append(s[i])
		j=i+1
		while(j<len(s)):
			if s[j] not in h:
				h.append(s[j])
			if len(h)==k:
				count+=1
				indexes.append((i, j))
			j+=1
		i+=1
	print indexes
	return count

def main():
	t = int(raw_input())
	while t:
		s, k = raw_input().split()
		print countExactlyKSubstrings(s, int(k))
		t-=1

if __name__ == '__main__':
	main()
	# print countExactlyKSubstrings("aba", 2)
	# print countExactlyKSubstrings("abcaa", 3)
