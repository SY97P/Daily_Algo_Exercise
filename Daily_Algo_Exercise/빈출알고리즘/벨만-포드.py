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

# 벨만-포드 알고리즘 (Bellman-Ford Algorithm)
# - 시작점~도착점 최단경로비용 구하는 문제
# - 힙큐x, DP o, 반복문(V*E) 사용
# - 다익스트라 알고리즘과의 차이점
# 	- 시간복잡도 : 다익스트라( O(E log V) ) < 벨만포드( O(V*E) )
# 	- 음수 간선 가중치가 있는 경우에도 최적해 도출 가능 (다익스트라는 불가능)
# 	- 음수 순환 감지 가능 (다익스트라는 음수 순환 있는 경우 무한루프에 빠짐)
# - 기본로직
# 	1. 정점의 수 만큼 반복
# 	2. 매 정점마다 간선정보를 순회하면서 dp값 갱신
# 	3. 마지막 정점 순회 중 dp값이 갱신되면 음수순환 존재 (갱신되지 않으면 음수순환 부재)

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

for tc in range(5) : 
	n, m = map(int, input().split())
	edges = [tuple(map(int, input().split())) for _ in range(m)]

	print(tc, "번째 TC")
	print("정점, 간선 수 : ", n,m)
	print("간선정보      : ", edges)
	
	INF = float('inf')
	dp = [INF for _ in range(n+1)]

	start = 1

	print("음수순환 여부 : ", end = "")
	print("존재" if bellman_ford(n, start, edges) else "부재")
	
	print("DP 프린트     : ", dp)
	print()
	
file.close()