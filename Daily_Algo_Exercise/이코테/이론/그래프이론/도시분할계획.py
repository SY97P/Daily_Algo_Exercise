n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(parent, num):
	if parent[num] != num:
		parent[num] = num

for _ in range(m):
	a, b, c = map(int, input().split())
	