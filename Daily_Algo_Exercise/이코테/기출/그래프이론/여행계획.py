n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

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

for a in range(n):
	for b in range(n):
		if matrix[a][b] == 1:
			if find(parent, a) != find(parent, b):
				union(parent, a, b)

answer = True 
for i in range(m-1):
	if find(parent, plan[i]-1) != find(parent, plan[i+1]-1):
		answer = False
		break
		
print("YES" if answer else "NO")

	