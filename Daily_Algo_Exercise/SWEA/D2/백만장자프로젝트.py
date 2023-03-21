file = open("./SWEA/D2/백만장자프로젝트.txt", "r")

input = file.readline

t = int(input())
for tc in range(1, t + 1) :
	n = int(input())
	prices = list(map(int, input().split()))
	print(n, prices)

	profit, highest = 0, 0
	for i in reversed(range(n)) : 
		if highest < prices[i] : 
			highest = prices[i]
		else : 
			profit += highest - prices[i]

	print("#%d %d" % (tc, profit))

file.close()