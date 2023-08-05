# * 위상정렬
# - 방향그래프의 모든 노드를 방향성을 위배하지 않도록 순서대로 나열하는 알고리즘
# - 진입차수 기록한 리스트 필요(정점개수+1)
# - 위상정렬 결과 개수와 정점수는 일치해야 함. (불일치 시 사이클 발생한 것)
# - 큐에 넣을 정점이 여러 개일 수 있기 때문에 결과가 다양할 수 있다. 
# 1. 진입차수 리스트, 인접리스트 생성
# 2. 진입차수가 0인 노드를 큐에 추가
# 3. 현재 노드에서 출발하는 간선 정보를 모두 지우기(연결된 정점의 진입차수 줄이기)
# 4. 새롭게 진입차수가 0이 되는 정점을 큐에 추가 

from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n+1)

adj = [[] for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)
	indegree[b] += 1

def topology_sort():
	result = []
	
	q = deque([])
	
	for i in range(1, n+1):
		if indegree[i] == 0:
			q.append(i)
	
	while q: 
		node = q.popleft()
		result.append(node)
		for next_node in adj[node]:
			indegree[next_node] -= 1
			if indegree[next_node] == 0:
				q.append(next_node)

	print(result)
	
topology_sort()

