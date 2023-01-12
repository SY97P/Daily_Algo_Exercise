# LL
# L
# DDDD

file = open("./백준/dp/역추적/DSLR.txt", "r")

input = file.readline

from collections import deque

n = int(input())

def solve(q) : 
	maxCount = float('inf')

	rtnLog = []

	while q : 
		item, log = q.popleft()

		if item == b : 
			if maxCount > dp[item] : 
				maxCount = dp[item]
				rtnLog = log
			continue

		if maxCount < dp[item] + 1 and dp[item] != float('inf') :
			continue

		for i in range(4) : 
			result = operation(i, item)
			if dp[item] + 1 < dp[result] : 
				dp[result] = dp[item] + 1
				q.append((result, log + [i]))

	return rtnLog

def operation(command, value) : 
	if command == 0 : 
		return (value * 2) % 10000
	elif command == 1 : 
		return value - 1 if value != 0 else 9999
	elif command == 2 : 
		return (value%1000)*10 + (value//1000)
	elif command == 3 : 
		return (value%10)*1000 + (value//10)
	else : 
		print("It cannot be")

for tc in range(n) :
	a, b = map(int, input().split())

	dp = [float('inf') for _ in range(10 ** 4)]
	dp[a] = 0

	log = solve(deque([(a, [])]))

	# print(dp[b])

	for l in log : 
		if l == 0 : 
			print("D", end = "")
		elif l == 1 : 
			print("S", end = "")
		elif l == 2: 
			print("L", end = "")
		elif l == 3 : 
			print("R", end = "")
		else : 
			print("")
	print()

file.close()