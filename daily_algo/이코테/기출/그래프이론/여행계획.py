file = open("./Daily_Algo_Exercise/이코테/기출/그래프이론/여행계획.txt")

input = file.readline

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
	elif fa > fb:
		parent[fa] = fb

for i in range(n):
	line = list(map(int, input().split()))
	for j in range(n):
		if line[j] == 1:
			union(parent, i+1, j+1)

path = list(map(int, input().split()))
answer = True
for i in range(m-1):
	if find(parent, path[i]) != find(parent, path[i+1]):
		answer = False
		break
print("YES" if answer else "NO")


file.close()