file = open("./dfs/바이러스tc.txt", "r")

def dfs(node, visited) : 
	# 종료조건 없어도 될 것 같음

for _ in range(1) : 
	v = int(file.readline())
	e = int(file.readline())
	edges = [list(map(int, file.readline().split())) for _ in range(e)]
	answer = int(file.readline())
	file.readline()

	print("v, e, answer : ", v, e, answer)
	for edg in edges : print(edg)
	print()

	visited = [False for _ in range(n+1)]

	dfs(1, visited)

	print(visited)
	

file.close()