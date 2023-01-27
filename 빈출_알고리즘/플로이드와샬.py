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

# * 플로이드 와샬 알고리즘
# 	1. 모든 출발점 -> 모든 도착점 최소 비용 구하기
# 	2. 분할정복 d[i][j] = min(d[i][j], d[i][k] + d[k][j]) k는 경유지
# 	3. 연산 전에 인접행렬을 dp에 초기화해줘야 함. -> 그래야 분할 정복이 가능
# 	4. 반복문 세 개로 해결 (경유지, 출발지, 도착지) -> O(n^3) ; DFS, BFS 아님!!

# 	- 다익스트라 알고리즘으로 해결하려고 하면 오답이 나옴
# 		- 모든 출발점 고려 시에는 최적해 보장이 안 되는 모양임.
# 		- 아마 경유지 고려를 안 하기 때문이 아닐까

# 	- 역추적하는 방법
# 		1. 경유지 선택 시 해당 경유지를 기록하는 dp와 동일 차원 배열 생성
# 		2. DFS를 이용해 divide and merge 해서 경로를 생성
# 		3. path = [start] + tracking(start, end) + [end]
# 			tracking(start, end) = return tracking(s, w) + [w] + tracking(w, e)
# 		4. track[i][j] 이 초기값이라면 경유지가 없다는 의미 -> 빈 리스트 반환
# 		5. 이동하는 경로가 존재하지 않음에도 track만 본다면 경로가 있음으로 판단하므로, dp[i][j] 가 초기값이 아닌지도 함께 확인

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