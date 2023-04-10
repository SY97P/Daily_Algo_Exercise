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

for _ in range(m):
	o, a, b = map(int, input().split())

	if o == 0:
		union(parent, a, b)
	else:
		if find(parent, a) == find(parent, b):
			print("YES")
		else:
			print("NO")