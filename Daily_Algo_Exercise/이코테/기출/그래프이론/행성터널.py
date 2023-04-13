file = open("./Daily_Algo_Exercise/이코테/기출/그래프이론/행성터널.txt")

input = file.readline 

import time

start_time = time.time()

n = int(input())
x, y, z = [], [], []
for i in range(n):
	a, b, c = map(int, input().split())
	x.append((a, i))
	y.append((b, i))
	z.append((c, i))
x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
	edges.append((x[i+1][0] - x[i][0], x[i+1][1], x[i][1]))
	edges.append((y[i+1][0] - y[i][0], y[i+1][1], y[i][1]))
	edges.append((z[i+1][0] - z[i][0], z[i+1][1], z[i][1]))
edges.sort()

end_time = time.time()

print("lap : ", end_time - start_time)

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
		answer += c

print(answer)

end_time = time.time()

print("time : ", end_time - start_time)

file.close()