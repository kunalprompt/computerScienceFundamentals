'''
Given a sequence of N numbers.
Find the length of the longest non-decreasing sequence.
'''

def main():
	numbers = map(int, raw_input().split())

	numbers_len = [0]*(len(numbers)+1)
	numbers_len[0] = 1
	for i in range(1, len(numbers)):
		if numbers[i] > numbers[i-1]:
			numbers_len[i] = numbers_len[i-1] + 1
		else:
			numbers_len[i] = 1
	print max(numbers_len)


if __name__ == "__main__":
	main()


'''
Example: 0 1 3 2 3 4 5 6 7 3 4
Indices: 0 1 2 3 4 5 6 7 8 9 10

Index | Length of longest non-decreasing sequence at Index

0 | 0
1 | 1
2 | 2
3 | 1
4 | 2
5 | 3
6 | 4
7 | 5
8 | 6
9 | 1
10 | 2

Max = 6
'''