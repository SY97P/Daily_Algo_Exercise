n = int(input())
coins = list(map(int, input().split()))
coins.sort()

won = 1
for i in range(n):
	if coins[i] <= won:
		won += coins[i]
	else:
		break 
print(won)