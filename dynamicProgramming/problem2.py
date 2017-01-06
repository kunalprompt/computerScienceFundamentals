'''
From a bag of n coins with multiple denominations, 
find the minimum number of coins required to get an amount S.

Example:
n = 3
coins = 1, 3, 5
S = 11

Output: 3 [5, 5, 1]
'''

def main():
	n = input()  # number of coins
	denominations = map(int, raw_input().split())  # list of coins
	if len(denominations) != n:
		return
	s = input()
	sum_coins_list = [0]*(s+1)

	for i in range(1, s+1):
		if i in denominations:
			sum_coins_list[i], max_den = 1, i  # max_den = maximum denomination in current
		else:
			rem_sum = i % max_den
			coins_used = i / max_den + sum_coins_list[rem_sum]
			coins_count = min(sum_coins_list[i-1] + 1, coins_used)
			sum_coins_list[i] = coins_count
	print sum_coins_list[s]

if __name__ == '__main__':
	main()


'''
Explanation:
sum | min no of coins 

0 | 0
1 | 1
2 | 2 (1)
3 | 1 (3)
4 | 2 (3, 1)
5 | 1 (5)
6 | 2 (5, 1)
7 | 3 (5, 1, 1)
8 | 2 (5, 3)
'''