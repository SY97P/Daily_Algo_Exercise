# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0

file = open('./백준/dp/역추적/플로이드2.txt', "r")

input = file.readline

import heapq
import sys 

input = sys.stdin.readline

def printDP() : 
	for i in range(1, n + 1) : 
		for d in dp[i][1:] :
			if d == float('inf') : 
				print(0, end = " ")
				continue
			print(d, end = " ")
		print()

def solve() : 
	for i in range(1, n + 1) : 
		for j in range(1, n + 1) :
			dp[i][j] = adj[i][j]
			
	for waypoint in range(1, n + 1) : 
		dp[waypoint][waypoint] = 0
		for start in range(1, n + 1) : 
			for end in range(1, n + 1) : 
				if dp[start][waypoint] + dp[waypoint][end] < dp[start][end] : 
					dp[start][end] = dp[start][waypoint] + dp[waypoint][end]


n = int(input())
m = int(input())

adj = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m) : 
	a, b, c = map(int, input().split())
	adj[a][b] = min(adj[a][b], c)

dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

solve()

printDP()

file.close()