# Prim Algorithm
# MST (Minimum Spanning Tree)
# O(e log V)
# 우선순위큐
# V > E 인 경우 효율적

file = open("./빈출알고리즘/?.txt", "r")

from collections import defaultdict
import heapq

input = file.readline

def prim(graph, node) : 
	# 재방문 방지
	visited[node] = True

	# heapq를 사용하면 O(e log V) 로 구할 수 있음.
	candi = graph[node]
	heapq.heapify(candi)

	# MST 연결 정보
	mst = []
	total_cost = 0

	while candi : 
		c, u, v = heapq.heappop(candi)

		if not visited[v] :
			visited[v] = True
			mst.append((u, v))
			total_cost += c

			for cost, next_u, next_v in graph[v] : 
				if not visited[next_v] :
					heapq.heappush(candi, (cost, next_u, next_v))

	return total_cost

v, e = map(int, input().split())
graph = defaultdict(list)
visited = [False for _ in range(v + 1)]

for _ in range(e) : 
	u, v, cost = map(int, input().split())
	graph[u].append([cost, u, v])
	graph[v].append([cost, v, u])

print(prim(graph, 1))