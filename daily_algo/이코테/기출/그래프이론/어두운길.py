file = open("./Daily_Algo_Exercise/이코테/기출/그래프이론/어두운길.txt")

input = file.readline 


n, m = map(int, input().split())
edges = []
total_cost = 0
for _ in range(m):
	a, b, c = map(int, input().split())
	total_cost += c
	edges.append((c, a, b))
edges.sort()

parent = [i for i in range(n+1)]

def find(parent, num):
	if parent[num] != num:
		parent[num] = find(parent, parent[num])
	return parent[num]

def union(parent, a, b):
	fa = find(parent, a)
	fb = find(parent, b)
	if fa < fb:
		parent[fb] = fa
	elif fa > fb:
		parent[fa] = fb

need_cost = 0
for c, s, e in edges:
	if find(parent, s) != find(parent, e):
		need_cost += c
		union(parent, s, e)
print(total_cost - need_cost)


file.close()