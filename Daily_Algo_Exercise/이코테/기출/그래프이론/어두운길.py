file = open("./Daily_Algo_Exercise/이코테/기출/그래프이론/어두운길.txt")

input = file.readline 

n, m = map(int, input().split())
edges = []
for _ in range(m):
	a, b, c = map(int, input().split())
	edges.append((c, a, b))
edges.sort()

parent = [i for i in range(n)]

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

answer = 0
for c, a, b in edges:
	if find(parent, a) != find(parent, b):
		union(parent, a, b)
	else:
		answer += c

print(answer)

file.close()