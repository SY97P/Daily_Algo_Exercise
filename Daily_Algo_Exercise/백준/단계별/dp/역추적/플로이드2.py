# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0
# 0
# 2 1 2
# 2 1 3
# 2 1 4
# 3 1 3 5
# 4 2 4 5 1
# 0
# 5 2 4 5 1 3
# 2 2 4
# 3 2 4 5
# 2 3 1
# 3 3 5 2
# 0
# 2 3 4
# 2 3 5
# 3 4 5 1
# 3 4 5 2
# 4 4 5 1 3
# 0
# 2 4 5
# 2 5 1
# 2 5 2
# 3 5 1 3
# 3 5 2 4
# 0

file = open("./백준/dp/역추적/플로이드2.txt", "r")

input = file.readline

import sys

input = sys.stdin.readline

def printDP() : 
	for i in range(1, n + 1) : 
		for j in range(1, n + 1) : 
			if dp[i][j] != float('inf') :
				print(dp[i][j], end = " ")
			else: 
				print(0, end = " ")
		print()

def trace() : 
	for start in range(1, n+1) : 
		for end in range(1, n+1) :
			if dp[start][end] in (0, float('inf')): 
				print(0)
				continue
			path = [start] + tracking(start, end) + [end]
			print(len(path), *path)

def tracking(start, end) :
	if track[start][end] == float('inf') :
		return []

	way = track[start][end]
	return tracking(start, way) + [way] + tracking(way, end)

def solve() : 
	for way in range(1, n + 1) : 
		dp[way][way] = 0
		for start in range(1, n + 1) : 
			for end in range(1, n + 1) : 
				if dp[start][end] > dp[start][way] + dp[way][end] : 
					dp[start][end] = dp[start][way] + dp[way][end]
					track[start][end] = way

n = int(input())
m = int(input())

track = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
adj = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m) : 
	a, b, c = map(int, input().split())
	adj[a][b] = min(adj[a][b], c)
	dp[a][b] = adj[a][b]

solve()

printDP()

trace()

file.close()