# Kruskal Algorithm
# MST (Minimum Spanning Tree) : 최소신장트리
# ST : 모든 v 연결, Cycle 없음(트리)
# M  : 가중치 합이 최소
# Union + Find => 서로소 집합 구하기

file = open("./빈출알고리즘/?.txt", "r")

input = file.readline

# 해당 노드가 집합에 이미 속해있는지 판단하는 함수
# 서로소 성질을 통해 cycle을 막으려고 하는 거
def find_parent(parent, x) : 
	if parent[x] != x : 
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

# 두 노드가 서로소. 
# 즉, 연결해도(부모노드를 같게 해도) cycle이 생기지 않음이 보장되었으므로
# 두 트리를 합치는 것.
def union_parent(parent, a, b) : 
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b : 
		parent[b] = a
	else : 
		parent[a] = b

# 노드 수, 간선 수
v, e = map(int, input().split())

# 집합 = 서로소 집합
parent = [i for i in range(1, v + 1)]
# 간선 정보
edges = []

# 총 가중치 합 (최소가 되어야 함. -> MST)
total_cost = 0

for _ in range(e) : 
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()

for i in range(e) :
	cost, a, b = edges[i]
	# 두 노드의 부모가 같지 않아야 합칠 수 있음
	# 다시 말해 두 노드가 분리되어있어야 합칠 수 있음. 
	# cycle 방지.
	if find_parent(a) != find_parent(b) :
		union_parent(parent, a, b)
		total_cost += cost

print(total_cost)