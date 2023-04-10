n, m = map(int, input().split())

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
	else:
		parent[fa] = fb

edges = []
for _ in range(m):
	a, b, c = map(int, input().split())
	edges.append((c, a, b))
edges.sort()

result = 0
max_weight = 0
for c, a, b in edges:
	if find(parent, a) != find(parent, b):
		union(parent, a, b)
		result += c
		max_weight = max(max_weight, c)

print(result - max_weight)