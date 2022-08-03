file = open("./dfs/트리의지름tc.txt", "r")

n = int(file.readline())
adj = [[] for _ in range(n+1)]
for _ in range(n-1) :
	p, c, w = map(int, file.readline().split())
	adj[p].append((c, w))
	adj[c].append((p, w))
answer = int(file.readline())

print(n, answer)
for ad in adj : 
	print(ad)

maxValue = 0

# 1. 모든 노드를 기준으로
for node in range(1, n) :
	# 1 dpth는 모든 방향 DFS
	curr = [] # 여러개가 있어도 두개만 골라야 함
	visited = [False for i in range(n+1)]
	visited[node] = True
	for ad in adj[node] :
		visited[ad[0]] = True
		curr.append(dfs(ad, visited))
		visited[ad[1]] = False

	# 최대값은 무엇인고
	if maxValue < sum(curr[:2])

file.close()