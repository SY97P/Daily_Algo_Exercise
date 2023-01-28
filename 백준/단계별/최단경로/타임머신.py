# 4
# 3
# -1 (음수순환)
# 3
# -1 (경로부재)
# -2
# -4
# -1 (음수순환)

file = open("./백준/최단경로/타임머신.txt", "r")

input = file.readline

# 음수 순환이 있는 경우 -> True 반환
# 음수 순환이 없는 경우 -> False 반환
def bellman_ford(n, start, edges) : 
	dp[start] = 0
	
	for node in range(n) :
		for curr, next, cost in edges : 
			if dp[curr] != INF and dp[next] > dp[curr] + cost : 
				dp[next] = dp[curr] + cost
				if node == n-1 : 
					return True
	return False

# for tc in range(5) : 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INF = float('inf')
dp = [INF for _ in range(n+1)]

start = 1

if bellman_ford(n, start, edges) :
	print(-1)
else : 
	for d in dp[2:] : 
		if d == INF : 
			print(-1)
		else : 
			print(d)
	
file.close()