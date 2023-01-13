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
			# 도달 경로가 없는 경우 초기값 나옴 -> 0 으로 바꿔서 출력
			if d == float('inf') : 
				print(0, end = " ")
				continue
			print(d, end = " ")
		print()

def solve() : 
	# 인접행렬 DP에 매핑
	for i in range(1, n + 1) : 
		for j in range(1, n + 1) :
			dp[i][j] = adj[i][j]

	# 분할 정복
	for waypoint in range(1, n + 1) : 
		# 자기 자신으로 가는 경우는 무조건 최소 비용 0 
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