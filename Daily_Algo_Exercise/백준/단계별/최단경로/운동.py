# 3

file = open("./백준/최단경로/운동.txt", "r")

input = file.readline

# import sys 

# input = sys.stdin.readline

INF = float('inf')

def course() : 
	dist = INF
	for i in range(1, v+1) : 
		for j in range(1, v+1) :
			if i == j : 
				continue 
			dist = min(dist, dp[i][j] + dp[j][i])
	return dist if dist != INF else -1
			

def printDP() : 
	print("DP print")
	for d in dp[1:] : 
		print(d[1:])

def floyd_warshall() : 
	for w in range(1, v+1) : 
		for s in range(1, v+1) : 
			dp[s][s] = 0
			for e in range(1, v+1) : 
				if dp[s][e] > dp[s][w] + dp[w][e] : 
					dp[s][e] = dp[s][w] + dp[w][e]
				

v, e = map(int, input().split())

dp = [[INF for _ in range(v+1)] for _ in range(v+1)]
adj = [[0 for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e) :
	a, b, c = map(int, input().split())
	adj[a][b] = c
	dp[a][b] = c

# print(v, e)
# for ad in adj : 
# 	print(ad)

floyd_warshall()

print(course())

file.close()