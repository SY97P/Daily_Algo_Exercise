from itertools import cycle
def solution(n, k, coin) : 
	coin = cycle(reversed(coin))

	# for i in reversed(range(n)) : 
	# 	print(i)

	count = 0 
	while k > 0: 
		c = next(coin)
		while k >= c : 
			count += 1
			k -= c
	return count

def main() : 
	n, k, coin = 10, 4200,[1,5,10,50,100,500,1000,5000,10000,50000]
	n, k, coin = 10, 4790,[1,5,10,50,100,500,1000,5000,10000,50000]
	print("solution : ", solution(n, k, coin))

main()

# 백준 제출용
# n, k = map(int, input().split())
# coins = list()
# for i in range(n) : 
#     coins.append(int(input()))

# count = 0 
# for i in reversed(range(n)) :
#     count += k // coins[i]
#     k = k % coins[i]
# print(count)