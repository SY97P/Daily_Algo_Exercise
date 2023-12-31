g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

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
for _ in range(p):
	num = int(input())
	if find(parent, num) == 0:
		break
	else:
		union(parent, num, num-1)
	answer += 1

print(answer)